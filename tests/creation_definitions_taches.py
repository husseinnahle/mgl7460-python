from logging import Logger

from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.modeles.province_ou_territoire import ProvinceOuTerritoire
from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.definitions.traitement_tache import TraitementTache
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class CreationDefinitionsTaches:

    fabrique = Fabrique.get_singleton_fabrique()

    @classmethod
    def get_tache_eligibilite_emprunteur(cls) -> DefinitionTache:
        definition_tache: DefinitionTache = cls.fabrique.creer_definition_tache(
            nom="Vérifier éligibilité emprunteur",
            description="Cette tâche vérifie que la personne qui emprunte est éligible pour un prêt",
        )
        definition_tache.set_traitement_tache(
            TraitementTache(
                lambda demande, logger: (demande.get_demandeur_pret().get_revenu_annuel() >= 35000.0)
                and (demande.get_demandeur_pret().get_taux_endettement() <= 0.37)
                and (demande.get_demandeur_pret().get_score_credit() >= 700)
            )
        )
        return definition_tache

    @classmethod
    def get_tache_eligibilite_propriete(cls) -> DefinitionTache:
        tache_eligibilite_propriete = cls.fabrique.creer_definition_tache(
            nom="Vérifier éligibilité propriété", description="Cette tâche vérifie l'éligibilité de la propriété"
        )
        tache_eligibilite_propriete.set_traitement_tache(
            TraitementTache(
                lambda demande, logger: demande.get_propriete().get_adresse().province() == ProvinceOuTerritoire.QUEBEC
            )
        )
        return tache_eligibilite_propriete

    @classmethod
    def get_tache_eligibilite_pret(cls) -> DefinitionTache:
        tache_eligibilite_pret = cls.fabrique.creer_definition_tache(
            nom="Éligibilité prêt",
            description="Cette tâche vérifie l'éligibilité du prêt en termes de mise de fonds et LTV",
        )
        tache_eligibilite_pret.set_traitement_tache(
            TraitementTache(
                lambda demande, logger: (demande.get_ratio_emprunt_valeur() <= 0.95)
                and (demande.get_montant_mise_de_fonds() > 0.05 * demande.get_montant_pret())
            )
        )
        return tache_eligibilite_pret

    @classmethod
    def get_tache_affichage_erreur(cls) -> DefinitionTache:
        tache_affichage_erreurs = cls.fabrique.creer_definition_tache(
            nom="Affichage messages d'erreur",
            description="Cette tâche affiche les messages d'erreur des différents traitements",
        )

        def afficher_erreurs(demande: DemandePret, logger: Logger):
            logger.info("Nous regrettons de vous informer que votre demande a été refusée pour les raisons suivantes")
            for message in demande.get_resultat_traitement().get_messages():
                logger.info(message)
            return True

        tache_affichage_erreurs.set_traitement_tache(TraitementTache(afficher_erreurs))
        return tache_affichage_erreurs

    @classmethod
    def get_tache_acceptation(cls) -> DefinitionTache:
        tache_acceptation = cls.fabrique.creer_definition_tache(
            nom="Acceptation", description="Cette tâche affiche le message d'acceptation"
        )

        def afficher_acceptation(demande: DemandePret, logger: Logger):
            logger.info(
                "Félicitations! votre demande de prêt a été approuvée. Veuillez prendre contact avec votre agent pour finaliser les termes du prêt"
            )
            return demande.get_resultat_traitement().get_resultat() == Resultat.ACCEPTEE

        tache_acceptation.set_traitement_tache(TraitementTache(afficher_acceptation))
        return tache_acceptation
