package main

import (
	"fmt"
	"log"
	"os/exec"
	"strings"
)

//CMD_call sert à envoyer des commandes à la console
func CMD_call(commande string, debug bool) (string, error) {
	commande_split := strings.Split(commande, " ")
	cmd := exec.Command(commande_split[0], commande_split[1:]...)
	out, err := cmd.CombinedOutput()
	fmt.Printf("combined out:\n%s\n", string(out))
	if (err != nil) && (debug == true) {
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	return string(out), err
}

func main() {
	commandes1 := "docker build -t data-eng:latest ."
	commandes11 := "tree"
	commandes2 := "docker run --name PROJET -d -p 5000:5000 data-eng"
	tests := "conda run -n python37 python tests.py"
	commandes3 := "docker pause PROJET"
	commandes4 := "docker container rm --force PROJET"
	commandes5 := "docker image rm --force data-eng"
	commandes55 := "heroku login"
	commandes6 := "git add ."
	commandes7 := "git commit -m \"update\""
	commandes8 := "git push"
	commandes9 := "git push heroku HEAD:master"
	CMD_call(commandes11, true)
	CMD_call(commandes1, true)
	CMD_call(commandes2, true)
	_, err := CMD_call(tests, false)
	CMD_call(commandes3, true)
	CMD_call(commandes4, true)
	CMD_call(commandes5, true)
	if err == nil {
		fmt.Printf("Let's upload the git...")
		CMD_call(commandes55, true)
		CMD_call(commandes6, true)
		CMD_call(commandes7, true)
		fmt.Printf("Let's upload the github...")
		CMD_call(commandes8, true)
		fmt.Printf("Let's upload the heroku...")
		CMD_call(commandes9, false)
	}
}
