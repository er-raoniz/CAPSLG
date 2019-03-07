from django.db import models
from django import forms
import googlemaps
import json

# Create your models here.
gmaps = googlemaps.Client(key='AIzaSyAzFFPgX-GryNpheDClG-PpEr1OGuHm6OY')

CATEGORY_CHOICES = (
    ('GOPEN', 'General Open'),
    ('GOBC','General Other Backward Class(OBC)'),
    ('PWDC','Persons with Disabilities'),
    ('LOPEN', 'Ladies Open'),
    ('LOBCS', 'Ladies Other Backward Class(OBC)'),
)

INITIAL_BRANCH_CHOICES = (
    ('IT', 'Information Techonology'),
    ('Chemical', 'Chemical'),
    ('Computer', 'Computer Engineering'),
    ('Civil', 'Civil Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Production','Production'),
    ('Mechanical','Mechanical'),
    ('Textile','Textile'),
)

BRANCH_CHOICES = (
    ('IT', 'Information Techonology'),
    ('Computer', 'Computer Engineering'),
    ('Chemical', 'Chemical'),
    ('Civil', 'Civil Engineering'),
    ('Electrical', 'Electrical'),
    ('EXTC','EXTC'),
    ('ETRX','ETRX'),
    ('Production','Production'),
    ('Mechanical','Mechanical'),
    ('Textile','Textile'),
    ('DyestuffTechnology', 'Dyestuff Technology'),
    ('OleochemicalsandSurfactantsTechnology', 'Oleochemicals and Surfactants Technology'),
    ('PharmaceuticalsChemistryandTechnology', 'Pharmaceuticals Chemistry and Technology'),
    ('FibresandTextileProcessingTechnology','Fibres and Textile Processing Technology'),
    ('PolymerEngineeringandTechnology','Polymer Engineering and Technology'),
    ('SurfaceCoatingTechnology','Surface Coating Technology'),
    ('Instrumental','Instrumental'),
    ('BioMedical','Bio Medical'),
    ('Automobile','Automobile'),
    ('Instrumentation','Instrumentation'),
    ('BioTechnology','Bio Technology'),
    ('PrintingandPacking','Printing and Packing'),
    ('Mechatronics','Mechatronics'),
)

COLLEGE_CHOICES = (
    ("vjti", "Veermata Jijabai Technological Institute"),
    ("sp", "Sardar Patel College of Engineering"),
    ("spit", "Bhartiya Vidya Bhavan's Sardar Patel Institute of Technology"),
    ("ict","Institute of Chemical Technology"),
    ("kjsce","K.J.Somaiya College of Engineering"),
    ("kjit","K J Somaiya Institute of Engineering and Information Technology"),
    ("vik", "Vivekanand Education Society's Institute of Technology"),
    ("sa", "Mahavir Education Trust's Shah & Anchor Kutchhi Engineering College"),
    ("dbit","Don Bosco Institute of Technology"),
    ("djs","Dwarkadas J. Sanghvi College of Engineering(DJ)"),
    ("fcr","Fr. Conceicao Rodrigues College of Engineering"),
    ("ss", "Anjuman-I-Islam's M.H. Saboo Siddik College of Engineering"),
    ("rgit", "Manjara Charitable Trust's Rajiv Gandhi Institute of Technology"),
    ("rcr", "Rizvi Education Society's Rizvi College of Engineering"),
    ("bvc"," Bharati Vidyapeeth College of Engineering"),
    ("dmc","N.Y.S.S.'s Datta Meghe College of Engineering"),
    ("afrc","Agnel Charities' FR. C. Rodrigues Institute of Technology"),
    ("kc", "K.C. College of Engineering and Management Studies and Research"),
    ("kgc", "Konkan Gyanpeeth College of Engineering"),
    ("ltc","Lokmanya Tilak College of Engineering"),
    ("mgm","M.G.M.'s College of Engineering and Technology"),
    ("pvp","Padmabhushan Vasantdada Patil Pratishthans College of Engineering"),
    ("pit", "M.E.S Pillai's Institute of Information Technology, Engineering Media Studies and Research"),
    ("rait", "(RAIT)Ramrao Adik Edu Soc, Ramarao Adik Institute of Tech"),
    ("jc","Shivajirao S. Jondhale College of Engineering"),
    ("sies","S.I.E.S. Graduate School of Technology"),
    ("sfit","St. Francis Institute of Technology"),
    ("tec", "Terna Engineering College"),
    ("tcet", "Thakur College of Engineering and Technology"),
    ("tse","Thadomal Shahani Engineering College"),
    ("vit","Vidyalankar Institute of Technology"),
)

FEES = {'vjti':83805,
        'sp':85020,
        'spit':149000,
        'ict':81000,
        'kjsce':173680,
        'kjit':132605,
        'vik':107790,
        'sa':108000,
        'dbit':122770,
        'djs':134750,
        'fcr':145085,
        'ss':118890,
        'rgit':96470,
        'rcr':82000,
        'bvc':85750,
        'dmc':92500,
        'afrc':140000,
        'kc':130000,
        'kgc':99000,
        'lti':117856,
        'mgm':82500,
        'pvp':122960,
        'pit':117000,
        'rait':88000,
        'jc':86000,
        'sies':105500,
        'sfit':108210,
        'tec':90250,
        'tcet':121500,
        'tse':142500,
        'vit':136272
    }

LOCATION = (('vjti',19.0222181,72.8561212),
        ('sp',19.1238086,72.8361388),
        ('spit',19.1231776,72.8361154),
        ('ict',19.0239192,72.8575207),
        ('kjsce',19.072674,72.9006989),
        ('kjit',19.046146,72.871043),
        ('vik',19.0453383,72.8889431),
        ('sa',19.0482157,72.9116581),
        ('dbit',19.0812532,72.8885961),
        ('djs',19.1071059,72.8371074),
        ('fcr',19.044497,72.8204535),
        ('ss',18.9685103,72.8310249),
        ('rgit',19.1212761,72.8236961),
        ('rcr',19.066677,72.8248061),
        ('bvc',19.0264933,73.0550664),
        ('dmc',19.160322,72.995568),
        ('afrc',19.0755127,72.9917043),
        ('kc',19.1799297,72.9802716),
        ('kgc',18.9159029,73.343191),
        ('lti',19.105774,73.0072909),
        ('mgm',19.0163873,73.1046578),
        ('pvp',19.0504293,72.8784344),
        ('pit',18.990201,73.1276701),
        ('rait',19.0443847,73.0257006),
        ('jc',19.1979524,73.1082841),
        ('sies',19.042813,73.023078),
        ('sfit',19.2435526,72.8557971),
        ('tec',19.0296489,73.0166693),
        ('tcet',19.2061342,72.8745324),
        ('tse',19.0644647,72.8358602),
        ('vit',19.0215885,72.8707363))

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=15, widget=forms.Select(choices=CATEGORY_CHOICES))
    score = forms.IntegerField()
    college = forms.CharField(max_length=15, widget=forms.Select(choices=COLLEGE_CHOICES))
    # branch = forms.CharField(max_length=15, widget=forms.Select(choices=BRANCH_CHOICES))
    branch = forms.ChoiceField(choices=INITIAL_BRANCH_CHOICES)

class PredictCollege(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=15, widget=forms.Select(choices=CATEGORY_CHOICES))
    score = forms.IntegerField()
    branch = forms.ChoiceField(choices=BRANCH_CHOICES)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': "autocomplete form-control form-control-sm", 'id': "autocomplete-input"}))

class CollegeData(models.Model):
    def get_branch_name(self, branch_code):
        for b in BRANCH_CHOICES:
            if branch_code == b[0]:
                return b[1]

    def get_category_name(self, category_code):
        for c in CATEGORY_CHOICES:
            if category_code == c[0]:
                return c[1]

    def get_fees(self, college_code):
        return FEES[college_code]

    def get_college_name(self, college_code):
        for c in COLLEGE_CHOICES:
            if college_code == c[0]:
                return c[1]

    def get_dist_dur(self, college_code, origin_loc):
        for l in LOCATION:
            if college_code == l[0]:
                lat = l[1]
                lng = l[2]
                destination_loc = {'lat':lat, 'lng':lng}
                geocode_result = gmaps.distance_matrix(origins=origin_loc,destinations=destination_loc)
                distance = geocode_result['rows'][0]['elements'][0]['distance']['value']
                duration = geocode_result['rows'][0]['elements'][0]['duration']['text']

                return distance/1000, duration
