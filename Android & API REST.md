# Présentation

## Partie 1 : L'exploration des concepts

### Qu'est ce qu'une activité Android ?

Android est, avant tout, un système d’exploitation qui est utilisé par la majorité des smartphones (63%) et des tablettes. Le système d’exploitation Android va permettre d’animer ces appareils mobiles et d’en permettre l’utilisation dynamique.

Le développement et la création d'application permet d'être compatibles avec les smartphones et tablettes du même nom.

 La flexibilité d’Android permet de **créer une unique application qui peut être rapidement adaptable aux différents environnements (smartphones, tablettes, montres connectées)**.

La majeure partie des applications Android est distribuée via Google Play Store.

Les applications Android peuvent intégrer de nombreuses fonctionnalités :

* Fonctionnalités GPS
* Différentes langues
* Prise de rdv, de réservations et de gestion de calendriers
* Capacités d'impression
* Appareil photo
* Géolocalisation
* Réseaux sociaux

Cette liste non exhaustive montre déjà la large bande d'applications développables sous Android.

### ...mais une activité qu'est ce que c'est en clair ?

Dans l’univers Android, les activités (activity en anglais) font partie des objets les plus utilisés. Chaque écran que voit et manipule l’utilisateur est, en effet, implémenté par une classe qui hérite de la classe Activity. Il est donc primordial de parfaitement comprendre tous les concepts apportés par cette classe.

Le système, pour des raisons de priorisation d'activités (coup de téléphone), peut tuer une activité quand il a besoin de ressources. Pour cette raison, aucune activité ne peut penser pouvoir vivre jusqu'au bout de son traitement, elle doit être considérée comme un humain. Elle peut avoir un accident, être à l'hôpital et/ou mourir.

Une activité possède quatre états que sont :

- « Active » : l'activité est lancée par l'utilisateur, elle s'exécute au premier plan ;
- « En pause » : l'activité est lancée par l'utilisateur, elle s'exécute et est visible, mais elle n'est plus au premier plan. Une notification ou une autre activité lui a volé le focus et une partie du premier plan ;
- « Stoppée » : l'activité a été lancée par l'utilisateur, mais n'est plus au premier plan et est invisible. L'activité ne peut interagir avec l'utilisateur qu'avec une notification ;
- « Morte » :l'activité n'est pas lancée.

La classe Activity fait partie du package Android.app. Le point d’entrée d’une classe héritant d’Activity est la méthode onCreate : c’est la première méthode qui est appelée à la création de l’activité, et c’est typiquement dans cette méthode que le développeur doit faire les initialisations dont il a besoin. 

La méthode onCreate de la classe héritant d’Activity doit impérativement appeler la méthode onCreate de la classe parente.

En fonction de l'état de l'activité, le développeur a la possibilité de gérer celle-ci à l'aide des méthodes héritées de la classe Activity.

Parmi ces méthodes, on trouve:

* onCreate(): lorsque l'activité est créée

* onStart(): lorsque l'activité est démarrée (visible par l'utilisateur)

* onResume(): lorsque l'activité re-démarre après une pause

* onPause(): lorsque l'activité est en pause (non visible par l'utilisateur)

* onStop(): lorsque l'activité arrête

* onDestroy(): lorsque l'activité est détruite

  ![RÃ©sultat de recherche d'images pour "processus android activity"](https://jef.binomed.fr/binomed_docs/Prezs/AndroidDebutant/images/activity_lifecycle.png)

  ### L'API REST, qu'est ce que c'est ?

  L’API, pour Application Programming Interface, est la partie du programme qu’on expose officiellement au monde extérieur pour manipuler celui-ci. L’API est au développeur ce que l’User Interface est à l’utilisateur. Cette dernière permet d’entrer des données et de les récupérer la sortie d’un traitement. Initialement, une API regroupe un ensemble de fonctions ou méthodes, leurs signatures et ordre d’usage pour obtenir un résultat.

  Une API est une interface pour les applications, car un logiciel n’a pas de mains ni d’yeux pour interagir avec les interfaces physiques !

  Les API “REST”, qui sont propres et polyvalentes pour beaucoup de types d’échange d’information entre logiciels. REST signifie “Representational State Transfer”.

  Les API REST sont basées sur HTTP, qui signifie Hypertext Transfer Protocol. C’est ce qui est au cœur du web ! 

  C’est un protocole qui définit la communication entre les différentes parties du web. L’échange est basé sur des requêtes client et serveur. Un client lance une requête HTTP, et le serveur renvoie une réponse.

  Les API REST imitent la façon dont le web lui-même marche dans les échanges entre un client et un serveur. Une API REST est :
  
  - Sans état
  - Cacheable (avec cache = mémoire)
  - Orienté client-serveur
  - Avec une interface uniforme
- Avec un système de couche
  - Un code à la demande (optionnel)

  Le fait d’être “sans état” signifie que le serveur n’a aucune idée de l’état du client entre deux requêtes. Du point de vue du serveur, chaque requête est une entité distincte des autres. 

  Ensuite, le cache, pour les API REST,  met en jeu le même principe que pour le reste d’Internet : un client doit être capable de garder en mémoire des informations sans avoir constamment besoin de demander tout au serveur. Ce sont les concepts de base à comprendre sur REST, nous verrons les autres lorsque vos projets deviendront plus complexes.

  Les réponses du serveur pour les API REST peuvent être délivrées dans de multiples formats. JSON (JavaScript Object Notation) est souvent utilisé, mais XML, CSV, ou même RSS sont aussi valables.

  ![img](https://www.supinfo.com/articles/resources/213817/5642/1.png)

  

  ## Bibliographie

  ###### 1 https://www.axopen.com/developpement-application-android/

  ###### 2 https://mathias-seguy.developpez.com/tutoriels/android/comprendre-cyclevie-activite/

  ###### 3 https://www.supinfo.com/articles/single/2844-activites-android
  
  ###### 4 https://openclassrooms.com/fr/courses/3449001-utilisez-des-api-rest-dans-vos-projets-web/3501901-pourquoi-rest
  
  ######  5 https://openclassrooms.com/fr/courses/3449001-utilisez-des-api-rest-dans-vos-projets-web/3501906-quelques-exemples-d-api-rest