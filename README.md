# tp1

## prerequis
on commence par créer le fichier python qui va appeler l'API puis le Dockerfile qui va créer l'image Docker.

## commandes 
 - docker login
 - docker build -t image_tp1:tag
 - docker push image_tp1:tag
 - docker run --env latitude="99.999" --env longitude="-99.9999" --env API_KEY="aaca89a14b3698bbd46dd966b2fa436d" image_tp1:tag


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
