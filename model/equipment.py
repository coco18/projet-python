from model.place import Place

class Equipment:
    """docstring for equipment"""
    def __init__(self):
        """Initialization of the equipment"""
        self.id = None
        self.name_equipment = None
        self.num_place = None
        self.place = None

    def create_object(self, tab):
        """Creation of the equipment
    	:param tab: Array with the attribute of an equipment
    	:type tab: array
    	"""
        self.id = tab[4]
        self.name_equipment = tab[5]
        self.num_place = tab[2]

    def insert(self, db):
        """insert the equipment in a table
    	:param db: the database who contains the table
    	:type db: base
    	"""
        c = db.con.cursor()
        insert_query = "INSERT INTO equipment(id, name_equipment, num_place) VALUES (?, ?, ?)"
        c.execute(insert_query, (self.id, self.name_equipment, self.num_place))

    def search(self,db,texte):
        """Return all the equipments with their place for an activity
    	:param db: the database who contains the table
    	:type db: base
    	:param texte: name of the activity
    	:type texte: String
    	:return tab: array with the equipment
    	:rtype tab : Equipment[]
    	"""
        c = db.con.cursor()
        query = "SELECT * from equipment, place where equipment.num_place=place.id and equipment.id IN (SELECT id_equipment from equipmentactivity where id_activity in (SELECT id FROM activity  where name_activity = {0}))".format(texte)
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            e = Equipment()
            e.id = row[0]
            e.name_equipment = row[1]
            e.num_place = row[2]
            e.place = Place()
            e.place.id = row[3]
            e.place.name_place = row[4]
            e.place.num_street = row[5]
            e.place.street = row[6]
            e.place.place_says = row[7]
            e.place.city = row[8]
            e.place.city_code = row[9]
            e.place.longitude = row[10]
            e.place.latitude = row[11]
            tab.append(e)
        return tab

    def select(self, db, idequipment):
        """Assign the value of the equipment passes in parameters to the actual equipment
    	:param db: the base who contains the table
    	:type db: base
    	:param idequipment: the identifiant of the equipment
    	:type idequipment: int
    	"""
        c = db.con.cursor()
        query = "SELECT * FROM equipment, place WHERE equipment.id={0} and equipment.num_place=place.id".format(idequipment)
        c.execute(query)
        row = c.fetchone()
        self.id = row[0]
        self.name_equipment = row[1]
        self.num_place = row[2]
        self.place = Place()
        self.place.id = row[3]
        self.place.name_place = row[4]
        self.place.num_street = row[5]
        self.place.street = row[6]
        self.place.place_says = row[7]
        self.place.city = row[8]
        self.place.city_code = row[9]
        self.place.longitude = row[10]
        self.place.latitude = row[11]
        print(self.place)

    def select_place_of_activity_in_city(self, DB, activity, city):
        """Give the existing equipment where you can practice an activity in a city
    	:param db: the base who contains the table
    	:type db: base
    	:param city: the name of the city
    	:type city: name
    	:returns: tab
    	:rtype: Equipment[]
    	"""
        c = DB.con.cursor()
        tab=[]
        lcity = "'"+city+"'"
        query = "SELECT * FROM equipment, place WHERE equipment.num_place=place.id and equipment.num_place in (SELECT id FROM place WHERE city={1}) and equipment.id in(SELECT id_equipment FROM equipmentactivity WHERE id_activity in(SELECT id FROM activity WHERE id={0}))".format(str(activity), lcity)
        c.execute(query)
        for row in c.fetchall():
            e = Equipment()
            e.id = row[0]
            e.name_equipment = row[1]
            e.num_place = row[2]
            e.place = Place()
            e.place.id = row[3]
            e.place.name_place = row[4]
            e.place.num_street = row[5]
            e.place.street = row[6]
            e.place.place_says = row[7]
            e.place.city = row[8]
            e.place.city_code = row[9]
            e.place.longitude = row[10]
            e.place.latitude = row[11]
            tab.append(e)
        return tab
#ComInsee,ComLib,InsNumeroInstall,InsNom,equipmentId,EquNom,EquNomBatiment,equipmentTypeLib,equipmentFiche,FamilleFicheLib,GestionTypeProprietairePrincLib,GestionTypeGestionnairePrincLib,GestionTypeProprietaireSecLib,GestionTypeGestionnaireSecLib,EquGestionDSP,EquDouche,EquEclairage,EquErpCTS,EquErpREF,EquErpL,EquErpN,EquErpO,EquErpOA,EquErpP,EquErpPA,EquErpR,EquErpRPE,EquErpSG,EquErpX,EquErpCategorie,EquAnneeService,AnneeServiceLib,EquNbPlaceTribune,NatureSolLib,NatureLibelle,EquHauteurEvolution,EquLongueurEvolution,EquLargeurEvolution,EquSurfaceEvolution,EquHauteurSurfaceEvo,EquNbCouloirPiste,EquNbVestiaireSpo,EquVestiaireSpoChauffe,EquNbVestiaireArbitre,EquSanitaireSportif,EquSanitairePublic,EquOuvertSaison,EquProximite,EquSono,EquTableauFixe,EquChrono,EquAmenagementAucun,EquUtilScolaire,EquUtilClub,EquUtilAutre,EquUtilIndividuel,EquUtilPerformance,EquUtilFormation,EquUtilRecreation,EquDateDernierTravauxReal,AnneeTravauxRealLibelle,EquDateDernierTravauxAucun,EquTravauxRealConformite,EquTravauxRealNorme,EquTravauxRealUsager,EquTravauxRealDegradation,EquTravauxRealVetuste,EquAccesHandimAire,EquAccesHandimTribune,EquAccesHandimVestiaire,EquAccesHandimSaniSpo,EquAccesHandimSaniPub,EquAccesHandimAucun,EquAccesHandisAucun,EquAccesHandisAire,EquAccesHandisTribune,EquAccesHandisVestiaire,EquAccesHandisSaniSpo,EquAccesHandisSaniPub,EquAccueilClub,EquAccueilSalle,EquAccueilBuvette,EquAccueilDopage,EquAccueilMedic,EquAccueilInfirmerie,EquAccueilBureau,EquAccueilReception,EquAccueilLocalRangement,EquAccueilAutre,EquAccueilAucun,EquChauffageNon,EquChauffageFuel,EquChauffageGaz,EquChauffageElectricite,EquChauffageSolaire,EquChauffageAutre,EquConfortSauna,EquConfortBainBouillonant,EquConfortBainVapeur,EquConfortSolarium,EquConfortAutre,EquConfortAucun,EquDemarcheHQE,EquSaeNbCouloir,EquSaeHauteur,EquSaeSurface,EquNatureSignal,EquNatureAlert,EquNatureAcPubPed,EquNatureAcPubRout,EquNatureAcPubMec,EquNatureAcPubNau,EquNatureAcSecPed,EquNatureAcSecRout,EquNatureAcSecMec,EquNatureAcSecNau,EquNatureLocTec,EquNatureLocPed,EquNatureAutorise,EquNaturePDESI,EquipNatureSituationLib,EquNatureSEVoies,EquNatureClassFedeMini,EquNatureClassFedeMaxi,EquNatureESTour,EquNatureAETreuil,EquNatureSKTotalRemontee,equipmentTir10,equipmentTir25,equipmentTir50,equipmentTir100,equipmentTir200,equipmentTir300,equipmentTirPlateau,equipmentTirAutre,EquAthDev,EquAthLongLigneDroite,EquAthNbCouloirLigne,EquAthNbCouloirHorsLigne,EquAthRiviere,EquNatSurv,EquAthNbSautTotal,EquAthNbSautHauteur,EquAthNbSautLongueur,EquAthNbSautTriple,EquAthNbSautPerche,EquAthNbLancerTotal,EquAthNbPoids,EquAthNbDisque,EquAthNbJavelot,EquAthNbMarteau,EquAthNBMarteauMixte,EquNatFormeLib,EquNatLongueurBassin,EquNatLargeurBassin,EquNatSurfaceBassin,EquNatProfMini,EquNatProfMax,EquNatCouloir,EquNatSurfacePlageBassin,EquNatNbTTotal,EquNatNbT1,EquNatNbT3,EquNatNbPTotal,EquNatNbP3,EquNatNbP5,EquNatNbP7,EquNatNbP10,EquNatMaV,EquNatTobog,EquNatPentaglisse,EquNatRiviere,EquNatImHandi,EquNatFM,EquNatMM,EquNatEclSub,EquNatSonorisationSub,EquNatAutre,EquPresencePataugeoir,EquGpsX,EquGpsY,EquDateMaj
