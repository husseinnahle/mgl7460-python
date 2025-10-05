from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.traitements.definitions.condition_transition import ConditionTransition
from mgl7460_tp1.types.traitements.definitions.definition_processus import DefinitionProcessus
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique
from tests.creation_definitions_taches import CreationDefinitionsTaches


class CreationDefinitionsProcessus:

    fabrique = Fabrique.get_singleton_fabrique()

    @classmethod
    def get_processus_lineaire(cls) -> DefinitionProcessus:
        processus_lineaire = cls.fabrique.creer_definition_processus(
            "Processus éligibilité simple",
            "Processus d'éeligibilité qui évalue les trois critères l'un à la suite de l'autre même si le premier échoue",
        )

        eligibilite_emprunteur = CreationDefinitionsTaches.get_tache_eligibilite_emprunteur()
        processus_lineaire.ajouter_premiere_tache(eligibilite_emprunteur)

        eligibilite_propriete = CreationDefinitionsTaches.get_tache_eligibilite_propriete()
        processus_lineaire.ajouter_tache(eligibilite_propriete)

        condition_transition = ConditionTransition(lambda tache_source, demande_pret: True)
        processus_lineaire.ajouter_transition_entre_taches(eligibilite_emprunteur, eligibilite_propriete, condition_transition)

        eligibilite_pret = CreationDefinitionsTaches.get_tache_eligibilite_pret()
        processus_lineaire.ajouter_tache(eligibilite_pret)

        processus_lineaire.ajouter_transition_entre_taches(eligibilite_propriete, eligibilite_pret, condition_transition)

        return processus_lineaire

    @classmethod
    def get_processus_errone(cls) -> DefinitionProcessus:

        processus_errone = cls.fabrique.creer_definition_processus(
            "Processus erroné",
            "Processus d'éeligibilité contenant deux transitions sortantes sans condition de la même tâche",
        )

        eligibilite_emprunteur = CreationDefinitionsTaches.get_tache_eligibilite_emprunteur()
        processus_errone.ajouter_premiere_tache(eligibilite_emprunteur)

        eligibilite_propriete = CreationDefinitionsTaches.get_tache_eligibilite_propriete()
        processus_errone.ajouter_tache(eligibilite_propriete)

        condition_transition = ConditionTransition(lambda tache_source, demande_pret: True)
        processus_errone.ajouter_transition_entre_taches(eligibilite_emprunteur, eligibilite_propriete, condition_transition)

        eligibilite_pret = CreationDefinitionsTaches.get_tache_eligibilite_pret()
        processus_errone.ajouter_tache(eligibilite_pret)

        processus_errone.ajouter_transition_entre_taches(eligibilite_emprunteur, eligibilite_pret, condition_transition)

        return processus_errone

    @classmethod
    def get_processus_complexe(cls) -> DefinitionProcessus:

        processus_complexe = cls.fabrique.creer_definition_processus(
            "Processus éligibilité complexe", "Processus d'éeligibilité qui sort dès que la demande échoue un critère"
        )

        eligibilite_emprunteur = CreationDefinitionsTaches.get_tache_eligibilite_emprunteur()
        processus_complexe.ajouter_premiere_tache(eligibilite_emprunteur)

        eligibilite_propriete = CreationDefinitionsTaches.get_tache_eligibilite_propriete()
        processus_complexe.ajouter_tache(eligibilite_propriete)

        eligibilite_pret = CreationDefinitionsTaches.get_tache_eligibilite_pret()
        processus_complexe.ajouter_tache(eligibilite_pret)

        affichage_erreurs = CreationDefinitionsTaches.get_tache_affichage_erreur()
        processus_complexe.ajouter_tache(affichage_erreurs)

        tache_acceptation = CreationDefinitionsTaches.get_tache_acceptation()
        processus_complexe.ajouter_tache(tache_acceptation)

        happy_condition = ConditionTransition(
            lambda tache_source, demande_pret: demande_pret.get_resultat_traitement().get_resultat()
            == Resultat.ACCEPTEE
        )

        processus_complexe.ajouter_transition_entre_taches(eligibilite_emprunteur, eligibilite_propriete, happy_condition)

        processus_complexe.ajouter_transition_entre_taches(eligibilite_propriete, eligibilite_pret, happy_condition)

        processus_complexe.ajouter_transition_entre_taches(eligibilite_pret, tache_acceptation, happy_condition)

        unhappy_condition = ConditionTransition(
            lambda tache_source, demande_pret: demande_pret.get_resultat_traitement().get_resultat()
            != Resultat.ACCEPTEE
        )

        processus_complexe.ajouter_transition_entre_taches(eligibilite_emprunteur, affichage_erreurs, unhappy_condition)

        processus_complexe.ajouter_transition_entre_taches(eligibilite_propriete, affichage_erreurs, unhappy_condition)

        processus_complexe.ajouter_transition_entre_taches(eligibilite_pret, affichage_erreurs, unhappy_condition)

        return processus_complexe
