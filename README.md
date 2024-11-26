# flask-app-swarm

## Création du service
```
docker service create --name <service-name> -p <host-port>:<container-port> <image-name>:<image-tag>
```

Exemple
```
docker service create --name flask-app -p 5000:5000 damienpm/flask-app-swarm:850eda27cd5460181efc99853479fb37c956da34
```

## Mise à jour de l'image
```
docker service update --image <image-name>:<image-tag> <service-name>
```

Exemple
```
docker service update --image damienpm/flask-app-swarm:... flask-app
```

## Création du réseau pour Flask App + DB
```
docker network create --driver=overlay --scope=swarm <network-name>
docker network create --driver=overlay --scope=swarm flask-app-network
```

## Création du service pour la base de données
```
docker service create --name flask-app-db \
  -e MYSQL_ROOT_PASSWORD=Passw0rd \
  -e MYSQL_DATABASE=flask-app \
  --network flask-app-network \
  mysql:9.1.0
```

## Création du service pour l'application python
```
docker service create --name flask-app-app \
  -e DB_HOST=flask-app-db \
  -e DB_USER=root \
  -e DB_PASSWORD=Passw0rd \
  -e DB_NAME=flask-app \
  -p 5000:5000 \
  --network flask-app-network \
  damienpm/flask-app-swarm:474a6ef101c10ed4ff6b5db90229775010beb080
```
