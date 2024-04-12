# devopstp1

## prerequis
on commence par créer le fichier python qui va appeler l'API puis le Dockerfile qui va créer l'image Docker.

## commandes 
 - docker login
 - docker build -t image_tp1:tag
 - docker push image_tp1:tag
 - docker run --env latitude="99.999" --env longitude="-99.9999" --env API_KEY="aaca89a14b3698bbd46dd966b2fa436d" image_tp1:tag
