# **Utilisation de Google Calendar**

Google Calendar est un outil qui permet de tenir son emploi du temps jour après jour.

## Pourquoi l'utilisons-nous ?

L'objectif d'utiliser Google Calendar est dans un premier temps de pratiquer l'utilisation d'un API. En effet, Google propose de nombreux API pour nombreuses de leurs applications. C'est le cas pour Google Calendar.

## Qu'allons-nous faire ?

Dans un premier temps, nous voulons afficher les éléments qui sont présents dans notre agenda.

## Qu'avons nous mis en place pour réussir cela ?

D'abord, il faut récupérer et importer les différentes bibliothèques et librairies nécessaires.

```python
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
```

Une fois ceci fait, on peut atteler à communiquer avec notre emploi du temps !!!

On va essayer d'afficher dans la console de notre IDE, les prochains cours qui sont programmés !

Pour ce faire, nous devons créer une application et obtenir un id et clé d'authentification qui sera utilisé dans le programme principal.

Ces accès sont stockés dans le fichier creditentials.json.

Le code afin de vérifier si les accès existent est :

```python
creds = None
    # Le fichier token.pickle stocke les identifiants de l'utilisateur et rafraîchit
    # les tokens et il va permettre de dérouler automatiquement la procédure de 
    # connexion à l'application créé à travers l'API Google Calendar
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si il n'y pas d'identifiants (valides) dispnibles, l'utilisateur va devoir se 
    # loger
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # On sauvegarde les identifiants pour les prochaines utilisations du 
        # programme
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
```

Ensuite, nous allons devoir récupérer nos données et nos cours exportés depuis Aurion.

Pour cela, on va appeler le Calendrier :

```python
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indique le temps en UTC
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
```

On affiche le paramètre 'summary' car c'est lui qui contient normalement le titre du cours.

Cependant, pour certaines données du calendrier, le programme plante car le summary est vide et ne contient aucune donnée.

Dans le cas où les 10 prochains événements sont correctement remplis au niveau du summary, on obtient l'affichage suivant :

![image-20191105232024624](C:\Users\Ervin\AppData\Roaming\Typora\typora-user-images\image-20191105232024624.png)

Voilà, maintenant il serait intéressant de repartir de ces données et de les ranger dans un json par exemple. Avec ce format, on pense qu'il serait possible de les exploiter et les utiliser pour faire une interface sous Android Studio.
