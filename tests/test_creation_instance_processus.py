from unittest import TestCase

from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.instances.exception_definition_processus import ExceptionDefinitionProcessus
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique
from tests.creation_definitions_processus import CreationDefinitionsProcessus
from tests.creation_definitions_taches import CreationDefinitionsTaches
from tests.creation_demandes_pret import CreationDemandesPret


class TestCreationInstanceProcessus(TestCase):

    fabrique = Fabrique.get_singleton_fabrique()

    def setUp(self):
        self.processus_lineaire = CreationDefinitionsProcessus.get_processus_lineaire()
        self.processus_complexe = CreationDefinitionsProcessus.get_processus_complexe()
        self.processus_errone = CreationDefinitionsProcessus.get_processus_errone()

    def a_echoue_les_taches(self, demande: DemandePret, definition_taches: list[DefinitionTache]) -> bool:
        messages = demande.get_resultat_traitement().get_messages()
        if len(messages) != len(definition_taches):
            return False
        matches_all = True
        for tache in definition_taches:
            nom_tache = tache.get_nom()
            matches_tache = False
            for message in messages:
                matches_tache = matches_tache or (nom_tache in message)
            matches_all = matches_all and matches_tache
        return matches_all

    def test_creation_instance_processus(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_oui_oui()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_lineaire, demande_pret)
        self.assertEqual(
            self.processus_lineaire,
            instance_processus.get_definition_processus(),
            "Le nouveau processus n'a pas la bonne definition",
        )

    def test_execution_processus_simple_sur_demande_oui_oui_oui(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_oui_oui()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_lineaire, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.ACCEPTEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être acceptée",
        )

    def test_execution_processus_simple_sur_demande_oui_oui_non(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_oui_non()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_lineaire, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.REFUSEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être refusée",
        )
        self.assertTrue(
            self.a_echoue_les_taches(demande_pret, [CreationDefinitionsTaches.get_tache_eligibilite_pret()])
        )

    def test_execution_processus_simple_sur_demande_oui_non_non(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_non_non()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_lineaire, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.REFUSEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être refusée",
        )
        self.assertTrue(
            self.a_echoue_les_taches(
                demande_pret,
                [
                    CreationDefinitionsTaches.get_tache_eligibilite_propriete(),
                    CreationDefinitionsTaches.get_tache_eligibilite_pret(),
                ],
            )
        )

    def test_execution_processus_simple_sur_demande_non_non_non(self):
        demande_pret = CreationDemandesPret.get_demande_pret_non_non_non()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_lineaire, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.REFUSEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être refusée",
        )
        self.assertTrue(
            self.a_echoue_les_taches(
                demande_pret,
                [
                    CreationDefinitionsTaches.get_tache_eligibilite_emprunteur(),
                    CreationDefinitionsTaches.get_tache_eligibilite_propriete(),
                    CreationDefinitionsTaches.get_tache_eligibilite_pret(),
                ],
            )
        )

    def test_execution_processus_simple_sur_demande_oui_non_oui(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_non_oui()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_lineaire, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.REFUSEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être refusée",
        )
        self.assertTrue(
            self.a_echoue_les_taches(demande_pret, [CreationDefinitionsTaches.get_tache_eligibilite_propriete()])
        )

    def test_processus_mal_forme(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_oui_oui()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_errone, demande_pret)
        with self.assertRaises(ExceptionDefinitionProcessus):
            instance_processus.demarrer()

    def test_execution_processus_complexe_sur_demande_oui_oui_oui(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_oui_oui()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_complexe, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.ACCEPTEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être acceptée",
        )

    def test_execution_processus_complexe_sur_demande_oui_oui_non(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_oui_non()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_complexe, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.REFUSEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être refusée",
        )
        self.assertTrue(
            self.a_echoue_les_taches(demande_pret, [CreationDefinitionsTaches.get_tache_eligibilite_pret()])
        )

    def test_execution_processus_complexe_sur_demande_oui_non_non(self):
        demande_pret = CreationDemandesPret.get_demande_pret_oui_non_non()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_complexe, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.REFUSEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être refusée",
        )
        self.assertTrue(
            self.a_echoue_les_taches(demande_pret, [CreationDefinitionsTaches.get_tache_eligibilite_propriete()])
        )

    def test_execution_processus_complexe_sur_demande_non_non_non(self):
        demande_pret = CreationDemandesPret.get_demande_pret_non_non_non()
        instance_processus = self.fabrique.creer_instance_processus(self.processus_complexe, demande_pret)
        instance_processus.demarrer()
        self.assertEqual(
            Resultat.REFUSEE,
            demande_pret.get_resultat_traitement().get_resultat(),
            f"La demande {demande_pret} devrait être refusée",
        )
        self.assertTrue(
            self.a_echoue_les_taches(demande_pret, [CreationDefinitionsTaches.get_tache_eligibilite_emprunteur()])
        )
