# tp1

## prerequis
on commence par créer le fichier python qui va appeler l'API puis le Dockerfile qui va créer l'image Docker.

## commandes 
 - docker login
 - docker build -t image_tp1:tag
 - docker push image_tp1:tag
 - docker run --env latitude="99.999" --env longitude="-99.9999" --env API_KEY="aaca89a14b3698bbd46dd966b2fa436d" image_tp1:tag

le problème que j'ai rencontré et mon imcapacité à me connecter à docker desktop due a des problèmes WSL.


# tp2 

## python
on utilise le framework Flask afin de créer notre API. Nous allons créer cette API puis définir les routes. 

## requirements
On ajoute ensuite le fichier requirements.txt afin de gérer les versions à télécharger pour l'image docker

## Docker 
on build ensuite l'image docker puis on la push sur docker hub. 
on run après l'image grâce à docker run. 

## workflow
On configure enfin le workflow github action afin de build et push l'image a chaque nouveau commit.

j'ai rencontré le même problème que lors du tp1.

# tp3
il s'agit de configurer le workflow github action pour créer l'image dans Azur cloud. je n'ai pas rencontré de problème particulier si ce n'est mon problème de connexion avec docker desktop.


# tp4

## terraform 
- on commence par définir les providers dans le dossier provider.tf
- on initialise ensuite les variables dans le fichier variables.tf
- on crée ensuite toutes les ressources dans le fichier main.tf
   - ressource pour générer la clé ssh
   - ressource pour créer l'interface réseau
   - ressource pour créer la machine virtuelle

## azure
- on se connecte en utilisant az login
