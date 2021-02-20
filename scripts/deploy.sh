GREEN="\033[0;32m"
NC="\033[0m"

APP_NAME=django_rest_starter
USER="simon"
REMOTEHOST="167.99.181.136"
TARGET="/home/${USER}/${APP_NAME}"
WHAT_TO_COPY=(instance scripts server src docker-compose.prod.yml)

start=$(date +%s)

echo -e "${GREEN}Deploying to server...${NC}"
echo -e "${GREEN}Ensure $TARGET exists in server...${NC}"
ssh $USER@$REMOTEHOST "mkdir -p ${TARGET}"

echo -e "${GREEN}Copying files to remote server...${NC}"
for i in "${WHAT_TO_COPY[@]}"; do
	rsync -r ./${i} $USER@$REMOTEHOST:$TARGET --delete
done

echo -e "${GREEN}Performing ssh into server.${NC}"
COMMANDS=(
"mv ${TARGET}/docker-compose.prod.yml ${TARGET}/docker-compose.yml"
"docker-compose -f ${TARGET}/docker-compose.yml down --remove-orphans"
"docker-compose -f ${TARGET}/docker-compose.yml up -d --build"
)
for i in "${COMMANDS[@]}"; do
	echo -e "${GREEN}Running: ${i} ${NC}"
	ssh ${USER}@${REMOTEHOST} "${i}"
done

end=$(date +%s)
runtime=$((end-start))
echo -e "${GREEN}Exec time: ${runtime}${NC}"
echo -e "${GREEN}Deployed to production${NC}"
