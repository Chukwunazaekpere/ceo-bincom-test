from django.db import models

from django.contrib.auth import get_user_model
Voters = get_user_model()


class States(models.Model):
    STATES = [
        ("1", 'Abuja'),
        ("2" , 'Abia'),
        ("3", 'Anambra'),
        ("4", 'Akwa Ibom'),
        ("5", 'Adamawa'),
        ("6", 'Bauchi'),
        ("7", 'Bayelsa'),
        ("8", 'Benue'),
        ("9", 'Borno'),
        ("10", 'Cross River'),
        ("12", 'Ebonyi'),
        ("13", 'Edo'),
        ("14", 'Ekiti'),
        ("15", 'Enugu'),
        ("16", 'Gombe'),
        ("17", 'Imo'),
        ("18", 'Jigawa'),
        ("19", 'Kaduna'),
        ("20", 'Kano'),
        ("21", 'Katsina'),
        ("22", 'Kebbi'),
        ("23", 'Kogi'),
        ("24", 'Kwara'),
        ("25", 'Delta'),
        ("26", 'Nasarawa'),
        ("27", 'Niger'),
        ("28", 'Ogun'),
        ("29", 'Ondo'),
        ("30", 'Osun'),
        ("31", 'Oyo'),
        ("32", 'Plateau'),
        ("33", 'Rivers'),
        ("34", 'Sokoto'),
        ("35", 'Taraba'),
        ("36", 'Yobe'),
        ("37", 'Zamfara'),
        ("251", 'Lagos')
    ]
    state_name = models.CharField(max_length=30, choices=STATES)
    state_id = models.CharField(max_length=5, help_text="This field is automatically populated. But you can input your preferred value, if need be.")

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self) -> str:
        return self.state_name


class Party(models.Model):
    PARTY_ID = [
        ('PDP', 'PDP'),
        ('DPP', 'DPP'),
        ('ACN', 'ACN'),
        ('PPA', 'PPA'),
        ('CDC', 'CDC'),
        ('JP', 'JP'),
        ('ANPP', 'ANPP'),
        ('LABOUR', 'LABOUR'),
        ('CPP', 'CPP')
    ]
    party_name = models.CharField(max_length=10, choices=PARTY_ID)
    party_id = models.CharField(max_length=7, help_text="This field is automatically populated. But you can input your preferred value, if need be.")

    def __str__(self) -> str:
        return f"{self.party_name} - {self.party_id}"

    
    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"

class LGA(models.Model):
    LGA_LIST = [
        ("Aniocha North", "Aniocha North"),
        ('Aniocha - South', 'Aniocha - South'),
        ('Ethiope East', 'Ethiope East'),
        ('Ethiope West', 'Ethiope West'),
        ('Ika North - East', 'Ika North - East'),
        ('Ika - South', 'Ika- South'),
        ('Isoko North', 'Isoko North'),
        ('Isoko South', 'Isoko South'),
        ('Ndokwa East', 'Ndokwa East'),
        ('Ndokwa West', 'Ndokwa West'),
        ('Okpe', 'Okpe'),
        ('Oshimili - North', 'Oshimili - North'),
        ('Oshimili - South', 'Oshimili - South'),
        ('Patani', 'Patani'),
        ('Sapele', 'Sapele'),
        ('Udu', 'Udu'),
        ('Ughelli North', 'Ughelli North'),
        ('Ughelli South', 'Ughelli South'),
        ('Ukwuani', 'Ukwuani'),
        ('Uvwie', 'Uvwie'),
        ('Bomadi','Bomadi'),
        ('Burutu','Burutu'),
        ('Warri North','Warri North'),
        ('Warri South','Warri South'),
        ('Warri South West', 'Warri South West'),
    ]
    lga_name = models.CharField(max_length=30, choices=LGA_LIST)
    lga_id = models.CharField(max_length=70, help_text="This field is automatically populated. But you can input your preferred value, if need be.")
    state = models.ForeignKey(States, related_name="state", verbose_name="State-Id", on_delete=models.CASCADE)
    lga_description = models.CharField(max_length=200)
    entered_by_user = models.ForeignKey(Voters, related_name="Voter", on_delete=models.SET_NULL, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    # `user_ip_address` varchar(50) NOT None,

    # def user_ip_address(self):
    class Meta:
        verbose_name = "LGA"
        verbose_name_plural = "LGA's"


class Ward(models.Model):
    WARD_DETAILS = [
        ("2", 'Aba - Unor'),
        ("8", 'Ejeme'),
        ("9", 'Isheagu - Ewulu'),
        ("7", 'Nsukwa'),
        ("2", 'Ogwashi - Uku I'),
        ("3", 'Ogwashi - Uku Ii'),
        ("1", 'Ogwashi - Uku Village'),
        ("4", 'Ubulu - Uku I'),
        ("5", 'Ubulu - Uku Ii'),
        ("11", 'Ubulu Okiti'),
        ("10", 'Ezi'),
        ("8", 'Idumuje - Unor'),
        ("5", 'Issele - Azagba'),
        ("6", 'Issele Uku I'),
        ("7", 'Issele Uku Ii'),
        ("1", 'Obior'),
        ("3", 'Obomkpa'),
        ("4", 'Onicha - Olona'),
        ("2", 'Onicha Ugbo'),
        ("9", 'Ukwu - Nzu'),
        ("0", 'Akugbene'),
        ("0", 'Akugbene Ii'),
        ("0", 'Akugbene Iii'),
        ("0", 'Bomadi'),
        ("0", 'Kolafiogbene / Ekametagbene'),
        ("0", 'Kpakiama'),
        ("0", 'Ogbeinama / Okoloba'),
        ("0", 'Ogo - Eze'),
        ("0", 'Ogriagene'),
        ("0", 'Syama'),
        ("0", 'Bolou - Ndoro'),
        ("0", 'Ngbilebiri'),
        ("0", 'Ngbilebiri Ii'),
        ("0", 'Obotebe'),
        ("0", 'Ogbolubiri'),
        ("0", 'Ogulagha'),
        ("0", 'Seimbiri'),
        ("0", 'Tamigbe'),
        ("0", 'Torugbene'),
        ("0", 'Tuomo'),
        ("1", 'Abraka I'),
        ("2", 'Abraka Ii'),
        ("3", 'Abraka Iii'),
        ("4", 'Agbon I'),
        ("5", 'Agbon Ii'),
        ("6", 'Agbon Iii'),
        ("7", 'Agbon Iv'),
        ("8", 'Agbon V'),
        ("9", 'Agbon Vi'),
        ("10", 'Agbon Vii'),
        ("11", 'Agbon Viii'),
        ("3", 'Jesse I'),
        ("4", 'Jesse Ii'),
        ("5", 'Jesse Iii'),
        ("6", 'Jesse Iv'),
        ("1", 'Mosogar I'),
        ("2", 'Mosogar Ii'),
        ("7", 'Oghara I'),
        ("8", 'Oghara Ii'),
        ("9", 'Oghara Iii'),
        ("10", 'Oghara Iv'),
        ("11", 'Oghara V'),
        ("10", 'Abavo I'),
        ("11", 'Abavo Ii'),
        ("12", 'Abavo Iii'),
        ("1", 'Agbor Town I'),
        ("2", 'Agbor Town Ii'),
        ("7", 'Boji - Boji I'),
        ("8", 'Boji - Boji Ii'),
        ("9", 'Boji - Boji Iii'),
        ("5", 'Ekuku - Agbor'),
        ("4", 'Ihiuiyase I'),
        ("6", 'Ihuiyase Ii'),
        ("3", 'Ihuozomor ( Ozanogogo Alisimie )'),
        ("7", 'Akumazi'),
        ("10", 'Idumuesah'),
        ("8", 'Igbodo'),
        ("12", 'Mbiri'),
        ("14", 'Otolokpo'),
        ("5", 'Owa V'),
        ("6", 'Owa Vi'),
        ("1", 'Owa I'),
        ("2", 'Owa Ii'),
        ("3", 'Owa Iii'),
        ("4", 'Owa Iv'),
        ("11", 'Umunede'),
        ("13", 'Ute - Ogbeje'),
        ("9", 'Ute - Okpu'),
        ("3", 'Ellu'),
        ("4", 'Emevor'),
        ("5", 'Iluelogbo'),
        ("1", 'Iyede I'),
        ("2", 'Iyede Ii'),
        ("8", 'Okpe - Isoko'),
        ("13", 'Otibio'),
        ("7", 'Ovrode',),
        ("6", 'Owhe / Akiehwe'),
        ("12", 'Oyede'),
        ("9", 'Ozoro I'),
        ("10", 'Ozoro Ii'),
        ("11", 'Ozoro Iii'),
        ("3", 'Aviara'),
        ("5", 'Emede'),
        ("9", 'Enhwe / Okpolo'),
        ("8", 'Erowa / Umeh'),
        ("7", 'Igbide',),
        ("11", 'Irri Ii'),
        ("10", 'Irri I'),
        ("1", 'Oleh I', ),
        ("2", 'Oleh Ii', ),
        ("6", 'Olomoro'),
        ("4", 'Uzere',),
        ("3", 'Abarra / Inyi / Onuaboh'),
        ("5", 'Aboh / Akarrai'),
        ("2", 'Afor / Obikwele'),
        ("7", 'Ase'),
        ("10", 'Ashaka'),
        ("8", 'Ibedeni'),
        ("9", 'Ibrede / Igbuku / Onogbokor',),
        ("4", 'Okpai / Utchi / Beneku'),
        ("6", 'Onyia / Adiai / Otuoku / Umuolu'),
        ("1", 'Ossissa'),
        ("9", 'Abbi Ii'),
        ("8", 'Abbi I'),
        ("10", 'Emu'),
        ("6", 'Ogume I'),
        ("7", 'Ogume Ii'),
        ("5", 'Onicha - Ukwani'),
        ("1", 'Utagba Ogbe'),
        ("2", 'Utagba Uno I'),
        ("3", 'Utagba Uno Ii'),
        ("4", 'Utagba Uno Iii'),
        ("5", 'Aghalokpe'),
        ("6", 'Aragba Town'),
        ("7", 'Mereje I'),
        ("8", 'Mereje Ii'),
        ("9", 'Mereje Iii'),
        ("3", 'Oha I', ),
        ("4", 'Oha Ii', ),
        ("1", 'Orerokpe'),
        ("2", 'Oviri - Okpe'),
        ("10", 'Ughoton'),
        ("1", 'Akwukwu'),
        ("2", 'Ebu'),
        ("4", 'Ibusa I', ),
        ("5", 'Ibusa Ii', ),
        ("6", 'Ibusa Iii', ),
        ("7", 'Ibusa Iv', ),
        ("8", 'Ibusa V', ),
        ("3", 'Illah'),
        ("9", 'Okpanam'),
        ("10", 'Ukala'),
        ("7", 'Agu'),
        ("2", 'Anala - Amakom'),
        ("10", 'Cable Point I'),
        ("11", 'Cable Point Ii'),
        ("1", 'Ogbele / Akpako',),
        ("3", 'Okwe'),
        ("7", 'Ugbomanta Quarters'),
        ("5", 'Umuaji'),
        ("4", 'Umuezei'),
        ("6", 'Umuonaje'),
        ("9", 'West End', ),
        ("1", 'Abari'),
        ("4", 'Agoloma'),
        ("8", 'Bolou - Angiama'),
        ("10", 'Odorubu / Adobu / Bolou Apelebri'),
        ("5", 'Patani Ii'),
        ("6", 'Patani Iii'),
        ("2", 'Patani I'),
        ("3", 'Taware / Kolowara Aven'),
        ("7", 'Toru - Angiama'),
        ("9", 'Uduophori'),
        ("9", 'Amuokpe'),
        ("3", 'Sapele Urban Iii'),
        ("4", 'Sapele Urban Iv'),
        ("5", 'Sapele Urban V'),
        ("6", 'Sapele Urban Vi'),
        ("7", 'Sapele Urban Vii'),
        ("8", 'Sapele Urban Viii'),
        ("1", 'Sapele Urban I'),
        ("2", 'Sapele Urban Ii'),
        ("10", 'Aladja'),
        ("6", 'Ekete'),
        ("5", 'Opete / Assagba / Edjophe'),
        ("9", 'Orhuwerun'),
        ("7", 'Ovwian I', ),
        ("8", 'Ovwian Ii', ),
        ("1", 'Udu I', ),
        ("2", 'Udu Ii', ),
        ("3", 'Udu Iii', ),
        ("4", 'Udu Iv', ),
        ("1", 'Agbarha'),
        ("10", 'Agbarho I', ),
        ("11", 'Agbarho Ii', ),
        ("8", 'Evwreni'),
        ("2", 'Ogor'),
        ("3", 'Orogun I', ),
        ("4", 'Orogun Ii', ),
        ("5", 'Ughelli I', ),
        ("6", 'Ughelli Ii', ),
        ("7", 'Ughelli Iii', ),
        ("9", 'Uwheru'),
        ("6", 'Effurun - Otor'),
        ("7", 'Ekakpamre'),
        ("8", 'Jeremi I'),
        ("9", 'Jeremi Ii'),
        ("10", 'Jeremi Iii'),
        ("4", 'Olomu I'),
        ("5", 'Olomu Ii'),
        ("2", 'Akoku'),
        ("6", 'Amai'),
        ("3", 'Ebedei'),
        ("5", 'Eziokpor'),
        ("6", 'Ezionum'),
        ("9", 'Obiaruku I'),
        ("10", 'Obiaruku Ii'),
        ("8", 'Umuebu'),
        ("4", 'Umukwata',),
        ("1", 'Umutu'),
        ("8", 'Army Barracks Area'),
        ("1", 'Effurun I'),
        ("2", 'Effurun Ii'),
        ("9", 'Ekpan I'),
        ("12", 'Ekpan Ii'),
        ("3", 'Enerhen I'),
        ("4", 'Enerhen Ii'),
        ("7", 'Ugbomro / Ugbolokposo'),
        ("5", 'Ugborikoko'),
        ("6", 'Ugboroke'),
        ("0", 'Ebrohimi'),
        ("0", 'Eghoro'),
        ("0", 'Gbokoda'),
        ("0", 'Isekelewu ( Egbema Ii )'),
        ("0", 'Koko I'),
        ("0", 'Koko Ii'),
        ("0", 'Ogbinbiri'),
        ("0", 'Ogbudugudu'),
        ("0", 'Ogheye'),
        ("0", 'Opuama'),
        ("0", 'Bowen'),
        ("0", 'Edjeba'),
        ("0", 'G.r.a'),
        ("0", 'Igbudu',),
        ("0", 'Obodo / Omadino'),
        ("0", 'Ode - Itsekiri'),
        ("0", 'Ogunu / Ekurede - Urhobo'),
        ("0", 'Okere'),
        ("0", 'Okumagba'),
        ("0", 'Okumagba Ii'),
        ("0", 'Pessu'),
        ("0", 'Ugbuwangue / Ekurede - Itsekiri'),
        ("0", 'Aja - Udaibo'),
        ("0", 'Akpikpa'),
        ("0", 'Gbaramatu'),
        ("0", 'Isaba'),
        ("0", 'Madangho'),
        ("0", 'Ogbe - Ijoh'),
        ("0", 'Ogidigben'),
        ("0", 'Oporoza'),
        ("0", 'Orere'),
        ("0", 'Ugborodo')
    ]

    ward_name = models.CharField(max_length=20, choices=WARD_DETAILS)
    ward_id = models.CharField(max_length=10, help_text="This field is automatically populated. But you can input your preferred value, if need be.")
    lga_id= models.ForeignKey(States, on_delete=models.CASCADE, help_text="If you can't find the LGA, then add it, using the green plus button")
    ward_description = models.CharField(max_length=200)
    entered_by_user = models.ForeignKey(Voters, on_delete=models.SET_NULL, null=True)
    date_entered = models.DateTimeField(auto_now_add=True, auto_now=False)
    #   user_ip_address varchar(50) NOT None,



class PollngUnit(models.Model):
    # POLL_UNIT_DATA = [
    #     (6, 'DT1708006', 'Sapele Ward 8 PU _', None),
    #     (4, 'DT1901004', 'Primary School in Aghara', 'Primary School in Aghara'),
    #     (5, 'DT1401005', 'Ishere Primary School  Aghara', 'Ishere Primary School Aghara'),
    #     (5, 'DT3403005', 'Igini Primary School', ' Esisi Road', '5.602005475', '6.001611141', None, None, None),
    #     (1, 'DT2104001', 'Umukwapa poll unit 1', None, '5.596383741', '5.99023883', None, None, None),
    #     (16,  'DT2201016', 'Church in Effurun1 Ovie', 'Church in Effurun1 Ovie', '5.59759314', '5.991187248', None, None, None),
    #     (6, 'DT1901006', 'Ishere Primary School Aghara', None, '5.90359853', '5.729595722', None, None, None),
    #     (13,  'DT2201013', 'Effurun 2 in Uvwie', 'Effurun 2 in Uvwie', '5.904090609', '5.729854354', None, None, None),
    #     (5, 7, 7, 59, 'DT0607005', 'school in ethiope west', 'school in ethiope west', '5.895063582', '5.730405695', None, None, None),
    #     (9, 1, 34, 242, 'DT3401009', 'agbasa 1', 'agbasa 1', '5.904748983', '5.725361522', None, None, None),
    #     (7, 1, 22, 223, 'DT2201007', 'Customary Court P.t.i Road', 'Customary Court P.t.i Road', '5.904025184', '5.735836456', None, None, None),
    #     (11, 2, 22, 224, 'DT2202011', 'effurun 2', 'effurun 2', '5.903925673', '5.736211371', None, None, None),
    #     (1, 9, 35, 262, 'DT3501001', 'asumbo town hall1', 'asumbo town hall1', '5.879748019', '5.73172331', None, None, None),
    #     (3, 2, 22, 224, 'DT2202003', 'eki-otoi', None, '5.876600455', '5.729696257', None, None, None),
    #     (3, 7, 6, 59, 'DT0607003', 'pollling 3 in agbara', 'pollling 3 in agbara', '5.900635513', '5.72786891', None, None, None),
    #     (6, 8, 6, 60, 'DT0608006', 'aghara ii', 'aghara ii', '5.879594849', '5.731894945', None, None, None),
    #     (4, 8, 6, 60, 'Dt0608004', 'aghara ii', 'aghara ii', '5.910613554', '5.768823319', None, None, None),
    #     (6, 9, 35, 262, 'DT3509006', 'obiteogbon quarters', 'obiteogbon quarters', '5.915854854', '5.775345359', None, None, None),
    #     (7, 9, 35, 262, 'DT3509007', 'okegbe quarter1', 'okegbe quarter1', '5.916066505', '5.775475401', None, None, None),
    #     (2, 7, 6, 59, 'DT0607002', 'agbasa 1', 'agbasa 1', '5.916323572', '5.775769489', None, None, None),
    #     (13, 3, 34, 244, 'DT340313', 'gra', 'gra', '5.916405598', '5.775643861', None, None, None),
    #     (14, 7, 6, 59, 'DT0607014', 'agbasa 1', 'agbasa 1', '5.976138434', '5.79185625', None, None, None),
    #     (8, 4, 1, 19, 'DT0104008', 'anocha north', 'anocha north', '5.976323443', '5.791971817', None, None, None),
    #     (12, 3, 34, 244, 'DT340312', 'gra ward', 'gra ward', '5.94474279', '5.749946582', None, None, None),
    #     (12, 7, 6, 59, 'DT0607012', 'school in ethiope west', 'school in ethiope west', '5.960247765', '5.787697717', None, None, None),
    #     (4, 3, 9, 90, 'DT0903004', 'ellu ', 'ellu ', '5.944916081', '5.749138498', None, None, None),
    #     (11, 9, 35, 262, 'DT3509011', 'emami quarter 2', 'emami quarter 2', '5.868711331', '5.753867466', None, None, None),
    #     (10, 9, 35, 262, 'DT3509010', 'emami quarter 1', 'emami quarter 1', '5.869546618', '5.752899868', None, None, None),
    #     (9, 9, 35, 262, 'DT3509009', 'oguanja quarters', 'oguanja quarters', '5.869563315', '5.753218155', None, None, None),
    #     (8, 9, 35, 262, 'DT3509008', 'okegbe quarters 2', 'okegbe quarters 2', '5.869457164', '5.753248025', None, None, None),
    #     (5, 9, 35, 262, 'DT3509005', 'obiteogbon quarters', 'obiteogbon quarters', '5.865254514', '5.754391377', None, None, None),
    #     (4, 9, 35, 262, 'DT3509004', 'ajudaibo primary school', 'ajudaibo primary school', '5.863768358', '5.754947902', None, None, None),
    #     (3, 9, 35, 262, 'DT3509003', 'ajudaibo primary school', 'ajudaibo primary school', '5.867018084', '5.750225876', None, None, None),
    #     (3, 4, 9, 91, 'DT0904003', 'isoko north', 'isoko north', '5.866359036', '5.746704932', None, None, None),
    #     (2, 9, 35, 262, 'DT3509002', 'hall 2', 'hall 2', '5.866407456', '5.746698042', None, None, None),
    #     (4, 7, 6, 59, 'DT0607004', 'school in ethiope west', 'school in ethiope west', '5.909925383', '5.794301233', None, None, None),
    #     (16, 2, 22, 224, 'DT220216', 'uvwie', 'uvwie', '5.878378164', '5.783819724', None, None, None),
    #     (6, 7, 6, 59, 'DT0607006', 'school in ethiope west', 'school in ethiope west', '5.861365948', '5.790962175', None, None, None),
    #     (14, 1, 19, 194, 'DT1901014', 'ughelli', 'ughelli', '5.861413666', '5.79088636', None, None, None),
    #     (2, 10, 15, 156, 'DT1510002', 'cable point i', 'cable point i', '5.861461099', '5.79080631', None, None, None),
    #     (3, 10, 15, 156, 'DT1510003', 'cable point i', 'cable point i', '5.880444551', '5.770730494', None, None, None),
    #     (4, 10, 15, 156, 'DT1510004', 'cable point i', 'cable point i', '5.878354903', '5.783820223', None, None, None),
    #     (5, 10, 15, 156, 'DT1510005', 'cable point i', 'cable point i', '5.878531591', '5.806744155', None, None, None),
    #     (6, 10, 15, 156, 'DT1510006', 'cable point i', 'cable point i', '5.878639525', '5.806654972', None, None, None),
    #     (7, 10, 15, 156, 'DT1510007', 'cable point i', 'cable point i', '5.878806006', '5.806560262', None, None, None),
    #     (8, 10, 15, 156, 'DT1510008', 'cable point i', 'cable point i', '5.879012412', '5.806466752', None, None, None),
    #     (9, 10, 15, 156, 'DT1510009', 'cable point i', 'cable point i', '5.867669536', '5.817836656', None, None, None),
    #     (10, 10, 15, 156, 'DT1510010', 'cable point i', 'cable point i', '5.867691306', '5.818044285', None, None, None),
    #     (11, 10, 15, 156, 'DT1510011', 'cable point i', 'cable point i', '5.867600201', '5.81823691', None, None, None),
    #     (15, 10, 15, 156, 'DT151015', 'cable point i', 'cable point i', '5.863066776', '5.830964841', None, None, None),
    #     (16, 10, 15, 156, 'DT151016', 'cable point i', 'cable point i', '5.873470151', '5.823753387', None, None, None),
    #     (17, 10, 15, 156, 'DT151017', 'cable point i', 'cable point i', '5.851069593', '5.836122533', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (8, 8, 22, 222, 'DT2288', 'aka avenue', 'aka avenue', '5.851158986', '5.836175239', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (8, 3, 17, 176, 'DT1738', 'sapele', 'sapele', '5.851270898', '5.836155212', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (13, 7, 6, 59, 'DT6713', 'ethiope', 'ethiope', '5.85144335', '5.836146137', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (5, 4, 1, 19, 'DT145', 'Aniocha North 4', 'Aniocha North 4', '5.863091905', '5.831179239', 'christian', '0000-00-00 00:00:00', '192.168.1.114'),
    #     (13, 3, 2, 6, 'DT2313', 'aniocha ward 3', 'aniocha ward 3', '5.866994163', '5.821855678', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (6, 4, 1, 19, 'DT146', 'aniocha ward 4', 'aniocha ward 4', '5.867741304', '5.817980929', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (21, 1, 22, 223, 'DT22121', 'uru standard junction off jakpa rd', 'uru standard junction off jakpa rd', '5.867601142', '5.818139328', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (1, 11, 15, 157, 'DT15111', 'Oshimili', 'Oshimili South', '5.807821471', '5.797203767', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (2, 11, 10, 108, 'DT10112', 'Isoko', 'Isoko South', '5.807754862', '5.797288301', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (3, 11, 15, 157, 'DT15113', 'Oshimili', 'Oshimili', '5.842704983', '5.786380747', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (4, 11, 15, 157, 'DT15114', 'Oshimili', 'Oshimili South', '5.842790118', '5.786331657', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (5, 11, 15, 157, 'DT15115', 'Oshimili', 'Oshimili South', '5.842864681', '5.78625909', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (6, 11, 15, 157, 'DT15116', 'Oshimili', 'Oshimili South', '5.842019519', '5.831029509', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (7, 11, 15, 157, 'DT15117', 'Oshimili', 'Oshimili South', '5.842620963', '5.831811301', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (1, 5, 10, 104, 'DT105001', 'Isoko', 'Isoko South', '5.837696181', '5.812672375', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (13, 10, 21, 218, 'DT211013', 'Ukwuani', 'Ukwuani ', '5.835630792', '5.824939901', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (3, 4, 21, 220, 'DT2143', 'Ukwuani', 'Ukwuani', '5.835483357', '5.824884533', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (6, 1, 22, 223, 'DT2216', 'Effurun', 'Effurun', '5.829120073', '5.825480729', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (11, 10, 21, 218, 'DT211011', 'Ukwuani', 'Ukwuani', '5.822940228', '5.835938252', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (7, 4, 1, 19, 'DT147', 'aniocha', 'aniocha', '5.785890606', '5.829924057', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (3, 0, 31, 28, 'DT3103', 'Bomadi', 'Bomadi', '5.822974806', '5.835903908', 'Dare', '0000-00-00 00:00:00', '192.168.1.114'),
    #     (5, 0, 31, 28, 'DT3105', 'Bomadi', 'Bomadi', '5.813067872', '5.850975385', 'Dare', '0000-00-00 00:00:00', '192.168.1.114'),
    #     (1, 0, 31, 28, 'DT310001', 'Bomadi', 'Bomadi', '5.813128721', '5.851046574', 'Dare', '0000-00-00 00:00:00', '192.168.1.114'),
    #     (3, 6, 13, 135, 'DT1363', 'Udogbie Village', 'Udogbie Village', '5.795222618', '5.83904385', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (8, 12, 22, 226, 'DT22128', 'aka avenue', 'aka avenue', '5.795293702', '5.839015885', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
    #     (3, 9, 6, 61, 'DT693', 'ethiope west ', 'ethiope west ', '5.801800496', '5.895480998', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (8, 8, 6, 60, 'DT688', 'ethiope', 'ethiope west ', '5.802012582', '5.895422869', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (2, 8, 6, 60, 'DT682', 'ethiope', 'ethiope west ', '5.802052137', '5.895223879', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (6, 10, 6, 62, 'DT6106', 'ethiope', 'ethiope west ', '5.800760234', '5.888332279', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (12, 9, 6, 61, 'DT6912', 'ethiope unit 12', 'ethiope unit 12', '5.800857495', '5.888584717', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (7, 0, 31, 26, 'DT3107', 'kolafiogbene', 'kolafio', '5.799316688', '5.892493172', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (11, 0, 31, 26, 'DT31011', 'kolafiogbene', 'kolafio', '5.799247669', '5.892551277', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (15, 0, 31, 26, 'DT31015', 'kolafiogbene', 'kolafiogbene', '5.949238684', '5.696328122', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (16, 0, 31, 26, 'DT31016', 'kolafiogbene', 'kolafiogbene', '5.949328101', '5.696164548', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (9, 0, 31, 30, 'DT3109', 'kolafiogbene', 'kolafiogbene', '5.948599325', '5.695844094', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (8, 0, 31, 30, 'DT3108', 'kolafiogbene', 'kolafiogbene', '5.947600862', '5.72692069', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (14, 0, 31, 26, 'DT31014', 'kolafiogbene', 'kolafiogbene', '5.9266113', '5.68939042', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (18, 0, 31, 26, 'DT31018', 'kolafiogbene', 'kolafiogbene', '5.926621717', '5.689337411', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (12, 0, 31, 26, 'DT31012', 'kolafiogbene', 'kolafiogbene', '5.926029293', '5.70101689', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    #     (4, 0, 31, 30, 'DT3104', 'kolafiogbene', 'kolafiogbene', '5.987535593', '5.77571573', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    # (6, 0, 31, 30, 'DT3106', 'kolafiogbene', 'kolafiogbene', '5.964548939', '5.710539049', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    # (10, 0, 31, 30, 'DT31010', 'kolafiogbene', 'kolafiogbene', '5.966931481', '5.714765312', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    # (51, 0, 31, 30, 'DT31051', 'kolafiogbene', 'kolafiogbene', '5.98954208', '5.76373367', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    # (21, 0, 31, 30, 'DT31021', 'kolafiogbene', 'kolafiogbene', '5.989685426', '5.76395642', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    # (31, 0, 31, 30, 'DT31031', 'kolafiogbene', 'kolafiogbene', '5.970365586', '5.731097122', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
    # (5, 5, 11, 115, 'DT1155', 'Ndokwa east', 'Ndokwa east', '5.948545677', '5.696001704', 'Dare', '0000-00-00 00:00:00', '192.168.1.111'),
    # (13, 0, 34, 244, 'DT34013', 'gra', 'gra', '5.953962649', '5.700047022', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
    # (12, 0, 34, 244, 'DT34012', 'gra', 'gra', '5.98539512', '5.764853605', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
    # (1, 0, 32, 38, 'DT3201', 'seimbiri', 'seimbiri', '5.989630887', '5.763867217', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
    # (6, 5, 11, 115, 'DT1156', 'ndokwa', 'ndokwa', '5.989745019', '5.764018125', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, entered_by_user0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ,
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', ),
    # (0, 0, 0, 0, '', '', '', )
    # ]

    polling_unit_name = models.CharField(max_length=70)
    polling_unit_id = models.PositiveIntegerField()
    polling_unit_number = models.PositiveIntegerField()
    polling_unit_description = models.CharField(max_length=200)
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE, verbose_name="Ward-Id", help_text="If you can't find the Ward, then add it, using the green plus button")
    lga_id = models.ForeignKey(LGA, on_delete=models.CASCADE, verbose_name="LGA-Id", help_text="If you can't find the LGA, then add it, using the green plus button")
    lattitude = models.CharField(max_length=70)
    longitude = models.CharField(max_length=70)
    entered_by_user = models.ForeignKey(Voters, related_name="Voters", on_delete=models.SET_NULL, null=True)

    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=70, verbose_name="User's IP-address")