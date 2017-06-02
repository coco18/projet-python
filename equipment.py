
class Equipment:
    """docstring for """
    def __init__(self):
        self.id = None
        self.name_equipment = None
        self.num_place = None

    """docstring for equipment"""
    def create_object(self, tab):
        self.id = tab[4]
        self.name_equipment = tab[5]
        self.num_place = tab[2]

    """insert equipment in database"""
    def insert(self, db):
        c = db.con.cursor()
        insert_query = "INSERT INTO equipment(id, name_equipment, num_place) VALUES (?, ?, ?)"
        c.execute(insert_query, (self.id, self.name_equipment, self.num_place))

    """search equipment in database"""
    def search(self,db,texte):
        c = db.con.cursor()
        query = "SELECT name_equipment from equipment where id IN (SELECT id_equipment from equipmentactivity where id_activity in (SELECT id FROM activity  where name_activity = {0}))".format(texte)
        c.execute(query)
        return c.fetchall()

    """select equipment in database"""
    def select(self,db idequipment):
        c = db.con.cursor()
        query = "SELECT * FROM equipment WHERE id={0} ".format(idequipment)
        c.execute(query)
        e = equipment()
        row = c.fetchone()
        e.id = row[0]
        e.name_equipment = row[1]
        e.num_place = row[2]
        return e

    def select_place_of_activity_in_city(self, activity, city):
        c = self.con.cursor()
        tab=[]
        num_place = list(self.select_num_place(city))
        for val in num_place:
            query = "SELECT * FROM equipment WHERE num_place ={1} and id in(SELECT id_equipment FROM equipmentactivity WHERE id_activity in(SELECT id FROM activity WHERE id={0}))".format(str(activity), val)
            c.execute(query)
            for row in c.fetchall():
                e = equipment()
                e.id = row[0]
                e.name_equipment = row[1]
                e.num_place = row[2]
                tab.append(e)
        return tab
#ComInsee,ComLib,InsNumeroInstall,InsNom,equipmentId,EquNom,EquNomBatiment,equipmentTypeLib,equipmentFiche,FamilleFicheLib,GestionTypeProprietairePrincLib,GestionTypeGestionnairePrincLib,GestionTypeProprietaireSecLib,GestionTypeGestionnaireSecLib,EquGestionDSP,EquDouche,EquEclairage,EquErpCTS,EquErpREF,EquErpL,EquErpN,EquErpO,EquErpOA,EquErpP,EquErpPA,EquErpR,EquErpRPE,EquErpSG,EquErpX,EquErpCategorie,EquAnneeService,AnneeServiceLib,EquNbPlaceTribune,NatureSolLib,NatureLibelle,EquHauteurEvolution,EquLongueurEvolution,EquLargeurEvolution,EquSurfaceEvolution,EquHauteurSurfaceEvo,EquNbCouloirPiste,EquNbVestiaireSpo,EquVestiaireSpoChauffe,EquNbVestiaireArbitre,EquSanitaireSportif,EquSanitairePublic,EquOuvertSaison,EquProximite,EquSono,EquTableauFixe,EquChrono,EquAmenagementAucun,EquUtilScolaire,EquUtilClub,EquUtilAutre,EquUtilIndividuel,EquUtilPerformance,EquUtilFormation,EquUtilRecreation,EquDateDernierTravauxReal,AnneeTravauxRealLibelle,EquDateDernierTravauxAucun,EquTravauxRealConformite,EquTravauxRealNorme,EquTravauxRealUsager,EquTravauxRealDegradation,EquTravauxRealVetuste,EquAccesHandimAire,EquAccesHandimTribune,EquAccesHandimVestiaire,EquAccesHandimSaniSpo,EquAccesHandimSaniPub,EquAccesHandimAucun,EquAccesHandisAucun,EquAccesHandisAire,EquAccesHandisTribune,EquAccesHandisVestiaire,EquAccesHandisSaniSpo,EquAccesHandisSaniPub,EquAccueilClub,EquAccueilSalle,EquAccueilBuvette,EquAccueilDopage,EquAccueilMedic,EquAccueilInfirmerie,EquAccueilBureau,EquAccueilReception,EquAccueilLocalRangement,EquAccueilAutre,EquAccueilAucun,EquChauffageNon,EquChauffageFuel,EquChauffageGaz,EquChauffageElectricite,EquChauffageSolaire,EquChauffageAutre,EquConfortSauna,EquConfortBainBouillonant,EquConfortBainVapeur,EquConfortSolarium,EquConfortAutre,EquConfortAucun,EquDemarcheHQE,EquSaeNbCouloir,EquSaeHauteur,EquSaeSurface,EquNatureSignal,EquNatureAlert,EquNatureAcPubPed,EquNatureAcPubRout,EquNatureAcPubMec,EquNatureAcPubNau,EquNatureAcSecPed,EquNatureAcSecRout,EquNatureAcSecMec,EquNatureAcSecNau,EquNatureLocTec,EquNatureLocPed,EquNatureAutorise,EquNaturePDESI,EquipNatureSituationLib,EquNatureSEVoies,EquNatureClassFedeMini,EquNatureClassFedeMaxi,EquNatureESTour,EquNatureAETreuil,EquNatureSKTotalRemontee,equipmentTir10,equipmentTir25,equipmentTir50,equipmentTir100,equipmentTir200,equipmentTir300,equipmentTirPlateau,equipmentTirAutre,EquAthDev,EquAthLongLigneDroite,EquAthNbCouloirLigne,EquAthNbCouloirHorsLigne,EquAthRiviere,EquNatSurv,EquAthNbSautTotal,EquAthNbSautHauteur,EquAthNbSautLongueur,EquAthNbSautTriple,EquAthNbSautPerche,EquAthNbLancerTotal,EquAthNbPoids,EquAthNbDisque,EquAthNbJavelot,EquAthNbMarteau,EquAthNBMarteauMixte,EquNatFormeLib,EquNatLongueurBassin,EquNatLargeurBassin,EquNatSurfaceBassin,EquNatProfMini,EquNatProfMax,EquNatCouloir,EquNatSurfacePlageBassin,EquNatNbTTotal,EquNatNbT1,EquNatNbT3,EquNatNbPTotal,EquNatNbP3,EquNatNbP5,EquNatNbP7,EquNatNbP10,EquNatMaV,EquNatTobog,EquNatPentaglisse,EquNatRiviere,EquNatImHandi,EquNatFM,EquNatMM,EquNatEclSub,EquNatSonorisationSub,EquNatAutre,EquPresencePataugeoir,EquGpsX,EquGpsY,EquDateMaj
