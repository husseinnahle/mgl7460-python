from logging import getLogger
from unittest import TestCase

from mgl7460_tp1.types.modeles.adresse import Adresse
from mgl7460_tp1.types.modeles.province_ou_territoire import ProvinceOuTerritoire
from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.traitements.definitions.condition_transition import ConditionTransition
from mgl7460_tp1.types.traitements.definitions.traitement_tache import TraitementTache
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class TestCreationDefinitionsProcessus(TestCase):

    fabrique = Fabrique.get_singleton_fabrique()

    nom_processus = "Vérification Éligibilité"
    description_processus = "Ce processus vérifie l'éligibilité du demandeur, de la propriété, et des termes du prêt"

    nom_tache_1 = "Éligibilité demandeur-se"
    description_tache_1 = "Cette tâche vérifie l'éligibilité de la personne demandeuse"

    nom_tache_2 = "Éligibilité propriété"
    description_tache_2 = "Cette tâche vérifie l'éligibilité de la propriété"

    nom_tache_3 = "Éligibilité prêt"
    description_tache_3 = "Cette tâche vérifie l'éligibilité de l'emprunt"

    def setUp(self):
        self.definition_processus = self.fabrique.creer_definition_processus(
            self.nom_processus, self.description_processus
        )

    def creer_demande_pret(self):
        demandeur = self.fabrique.creer_demandeur_pret("Jeanne", "Bergeron", "123-456-789", 120000, 40000, 765)
        propriete = self.fabrique.creer_propriete(
            adresse=Adresse("201A", "2100", "Saint-Urbain", "Montréal", ProvinceOuTerritoire.QUEBEC, "H2X2XH"),
            valeur_de_marche=400000,
        )
        return self.fabrique.creer_demande_pret(
            propriete=propriete, demandeur_pret=demandeur, prix_achat=405000, mise_de_fonds=30000
        )

    def tester_attributs_definition_processus(self):
        self.assertEqual(self.nom_processus, self.definition_processus.get_nom(), "Nom du processus mal initialisé")
        self.assertEqual(
            self.description_processus,
            self.definition_processus.get_description(),
            "Description du processus mal initialisée",
        )

    def tester_creation_definition_tache(self):
        definition_tache = self.fabrique.creer_definition_tache(self.nom_tache_1, self.description_tache_1)
        self.assertIsNotNone(definition_tache)
        self.assertEqual(self.nom_tache_1, definition_tache.get_nom(), "Nom définition tâche mal initialisé")
        self.assertEqual(
            self.description_tache_1, definition_tache.get_description(), "Description tâche mal initialisée"
        )

    def tester_ajout_premiere_definition_tache(self):
        definition_tache = self.fabrique.creer_definition_tache(self.nom_tache_1, self.description_tache_1)
        self.definition_processus.ajouter_tache(definition_tache)
        self.assertEqual(definition_tache, self.definition_processus.get_taches()[0], "La tache n'a pas été ajoutée")
        self.assertTrue(self.definition_processus.is_tache_finale(definition_tache), "Tache est supposée être finale")

    def tester_ajout_transition(self):
        # 1. Ajout tache 1
        definition_tache_1 = self.fabrique.creer_definition_tache(self.nom_tache_1, self.description_tache_1)
        self.definition_processus.ajouter_tache(definition_tache_1)
        # 2. Ajout tache 2
        definition_tache_2 = self.fabrique.creer_definition_tache(self.nom_tache_2, self.description_tache_2)
        self.definition_processus.ajouter_tache(definition_tache_2)
        # 3. Ajout tache 3
        definition_tache_3 = self.fabrique.creer_definition_tache(self.nom_tache_3, self.description_tache_3)
        self.definition_processus.ajouter_tache(definition_tache_3)
        # 4.a. Créer et ajouter une transition sans condition (toujours active)
        definition_transition = self.fabrique.creer_definition_transition(definition_tache_1, definition_tache_2)
        self.definition_processus.ajouter_transition(definition_transition)
        # 4.b. Créer et ajouter une transition avec condition
        condition_transition = ConditionTransition(lambda tache, demande: demande.get_ratio_emprunt_valeur() > 0.95)
        self.definition_processus.ajouter_transition_entre_taches(definition_tache_1, definition_tache_3, condition_transition)
        # 5. Verifier le nombre de transitions
        nombre_transitions_sortantes = len(self.definition_processus.get_transitions_sortantes_de(definition_tache_1))
        self.assertEqual(
            2, nombre_transitions_sortantes, f"Je m'attendais à 2 transitions sortantes de {self.nom_tache_1}"
        )
        # 6. Vérifier que les tâches 2 et 3 sont finales
        self.assertTrue(
            self.definition_processus.is_tache_finale(definition_tache_2), f"{self.nom_tache_2} devrait être finale"
        )
        self.assertTrue(
            self.definition_processus.is_tache_finale(definition_tache_3), f"{self.nom_tache_3} devrait être finale"
        )
        # 7. Vérifier que la tâche 1 n'est pas finale
        self.assertFalse(
            self.definition_processus.is_tache_finale(definition_tache_1),
            f"{self.nom_tache_1} ne devrait pas être finale",
        )

    def test_executer_definition_tache(self):
        # 1. Creer definition tache
        definition_tache = self.fabrique.creer_definition_tache(
            self.nom_tache_1,
            self.description_tache_1,
            TraitementTache(lambda demande, logger: demande.get_demandeur_pret().get_taux_endettement() <= 0.37),
        )
        # 2. Lecture de definition tache
        traitement_tache = definition_tache.get_traitement_tache()
        # 3. Creer une demande de prêt
        demande_pret = self.creer_demande_pret()
        # 4. Executer la tache
        logger = getLogger(f"Logger pour tache {self.nom_tache_1}")
        resultat = traitement_tache.traiter_demande_pret(demande_pret, logger)
        # 5. Vérifier le résultat
        self.assertTrue(resultat, "L'emprunteur devrait etre eligible")

    def test_executer_definition_transition(self):
        # 1. Ajouter de la premiere tache
        definition_tache_1 = self.fabrique.creer_definition_tache(self.nom_tache_1, self.description_tache_1)
        self.definition_processus.ajouter_tache(definition_tache_1)
        # 2. Ajouter de la deuxieme tache
        definition_tache_2 = self.fabrique.creer_definition_tache(self.nom_tache_2, self.description_tache_2)
        self.definition_processus.ajouter_tache(definition_tache_2)
        # 3. Ajouter une transition avec condition
        condition_transition = ConditionTransition(
            lambda tache, demande: demande.get_resultat_traitement().get_resultat() == Resultat.ACCEPTEE
        )
        definition_transition = self.fabrique.creer_definition_transition(
            definition_tache_1, definition_tache_2, condition_transition
        )
        self.assertEqual(
            condition_transition,
            definition_transition.get_condition_transition(),
            "La condition de transation est mal initialisée",
        )
        # 4. Executer la transition
        demande_pret = self.creer_demande_pret()
        demande_pret.set_resultat_traitement(self.fabrique.creer_resultat_traitement(Resultat.ACCEPTEE))
        condition_transition = definition_transition.get_condition_transition()
        resultat = condition_transition.is_transition_ok(None, demande_pret)
        self.assertTrue(resultat, f"Transition de {self.nom_tache_1} à {self.nom_tache_2} devrait être activee")
