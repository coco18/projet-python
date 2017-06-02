
class Equipment:
    """docstring for """
    def __init__(self):
        self.id = None
        self.name_equipment = None
        self.num_place = None

    """docstring for equipment"""
    def create_object(self, tab):
        self.id = tab[4]
        self.name_equipement = tab[5]
        self.num_place = tab[2]

    """insert equipment in database"""
    def insert(self, db):
        c = db.con.cursor()
        insert_query = "INSERT INTO equipment(id, name_equipment, num_place) VALUES (?, ?, ?)"
        c.execute(insert_query, (self.id, self.name_equipment, self.num_place))

    """search equipment in database"""
    def search(self,db,texte):
        c = db.con.cursor()
        query = "SELECT name_equipement from equipement where id IN (SELECT id_equipement from equipementactivity where id_activity in (SELECT id FROM activity  where name_activity = {0}))".format(texte)
        c.execute(query)
        return c.fetchall()

    """select equipment in database"""    
    def select(self,db idequipment):
        c = db.con.cursor()
        query = "SELECT * FROM equipement WHERE id={0} ".format(idequipment)
        c.execute(query)
        e = Equipement()
        row = c.fetchone()
        e.id = row[0]
        e.name_equipement = row[1]
        e.num_place = row[2]
        return e
#ComInsee,ComLib,InsNumeroInstall,InsNom,EquipementId,EquNom,EquNomBatiment,EquipementTypeLib,EquipementFiche,FamilleFicheLib,GestionTypeProprietairePrincLib,GestionTypeGestionnairePrincLib,GestionTypeProprietaireSecLib,GestionTypeGestionnaireSecLib,EquGestionDSP,EquDouche,EquEclairage,EquErpCTS,EquErpREF,EquErpL,EquErpN,EquErpO,EquErpOA,EquErpP,EquErpPA,EquErpR,EquErpRPE,EquErpSG,EquErpX,EquErpCategorie,EquAnneeService,AnneeServiceLib,EquNbPlaceTribune,NatureSolLib,NatureLibelle,EquHauteurEvolution,EquLongueurEvolution,EquLargeurEvolution,EquSurfaceEvolution,EquHauteurSurfaceEvo,EquNbCouloirPiste,EquNbVestiaireSpo,EquVestiaireSpoChauffe,EquNbVestiaireArbitre,EquSanitaireSportif,EquSanitairePublic,EquOuvertSaison,EquProximite,EquSono,EquTableauFixe,EquChrono,EquAmenagementAucun,EquUtilScolaire,EquUtilClub,EquUtilAutre,EquUtilIndividuel,EquUtilPerformance,EquUtilFormation,EquUtilRecreation,EquDateDernierTravauxReal,AnneeTravauxRealLibelle,EquDateDernierTravauxAucun,EquTravauxRealConformite,EquTravauxRealNorme,EquTravauxRealUsager,EquTravauxRealDegradation,EquTravauxRealVetuste,EquAccesHandimAire,EquAccesHandimTribune,EquAccesHandimVestiaire,EquAccesHandimSaniSpo,EquAccesHandimSaniPub,EquAccesHandimAucun,EquAccesHandisAucun,EquAccesHandisAire,EquAccesHandisTribune,EquAccesHandisVestiaire,EquAccesHandisSaniSpo,EquAccesHandisSaniPub,EquAccueilClub,EquAccueilSalle,EquAccueilBuvette,EquAccueilDopage,EquAccueilMedic,EquAccueilInfirmerie,EquAccueilBureau,EquAccueilReception,EquAccueilLocalRangement,EquAccueilAutre,EquAccueilAucun,EquChauffageNon,EquChauffageFuel,EquChauffageGaz,EquChauffageElectricite,EquChauffageSolaire,EquChauffageAutre,EquConfortSauna,EquConfortBainBouillonant,EquConfortBainVapeur,EquConfortSolarium,EquConfortAutre,EquConfortAucun,EquDemarcheHQE,EquSaeNbCouloir,EquSaeHauteur,EquSaeSurface,EquNatureSignal,EquNatureAlert,EquNatureAcPubPed,EquNatureAcPubRout,EquNatureAcPubMec,EquNatureAcPubNau,EquNatureAcSecPed,EquNatureAcSecRout,EquNatureAcSecMec,EquNatureAcSecNau,EquNatureLocTec,EquNatureLocPed,EquNatureAutorise,EquNaturePDESI,EquipNatureSituationLib,EquNatureSEVoies,EquNatureClassFedeMini,EquNatureClassFedeMaxi,EquNatureESTour,EquNatureAETreuil,EquNatureSKTotalRemontee,EquipementTir10,EquipementTir25,EquipementTir50,EquipementTir100,EquipementTir200,EquipementTir300,EquipementTirPlateau,EquipementTirAutre,EquAthDev,EquAthLongLigneDroite,EquAthNbCouloirLigne,EquAthNbCouloirHorsLigne,EquAthRiviere,EquNatSurv,EquAthNbSautTotal,EquAthNbSautHauteur,EquAthNbSautLongueur,EquAthNbSautTriple,EquAthNbSautPerche,EquAthNbLancerTotal,EquAthNbPoids,EquAthNbDisque,EquAthNbJavelot,EquAthNbMarteau,EquAthNBMarteauMixte,EquNatFormeLib,EquNatLongueurBassin,EquNatLargeurBassin,EquNatSurfaceBassin,EquNatProfMini,EquNatProfMax,EquNatCouloir,EquNatSurfacePlageBassin,EquNatNbTTotal,EquNatNbT1,EquNatNbT3,EquNatNbPTotal,EquNatNbP3,EquNatNbP5,EquNatNbP7,EquNatNbP10,EquNatMaV,EquNatTobog,EquNatPentaglisse,EquNatRiviere,EquNatImHandi,EquNatFM,EquNatMM,EquNatEclSub,EquNatSonorisationSub,EquNatAutre,EquPresencePataugeoir,EquGpsX,EquGpsY,EquDateMaj
