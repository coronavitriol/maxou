package main

import (
	"fmt"
	"log"
	"os/exec"
)

func CMD_call(commande []string) (string, error) {
	cmd := exec.Command(commande[0], commande[1:]...)
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	fmt.Printf("combined out:\n%s\n", string(out))
	return string(out), err
}

func main() {
	commandes1 := []string{"docker", "build", "-t", "data-eng:latest", "."}
	commandes2 := []string{"docker", "run", "--name", "PROJET", "-d", "-p", "5000:5000", "data-eng"}
	tests := []string{"python", "tests.py"}
	commandes3 := []string{"docker", "pause", "PROJET"}
	commandes4 := []string{"docker", "container", "rm", "--force", "PROJET"}
	commandes5 := []string{"docker", "image", "rm", "--force", "data-eng"}
	commandes6 := []string{"git", "add", "."}
	commandes7 := []string{"git", "commit", "-m", "update"}
	//commandes8 := []string{"git", "push"}
	commandes9 := []string{"git", "push", "heroku", "master"}
	CMD_call(commandes1)
	CMD_call(commandes2)
	CMD_call(tests)
	CMD_call(commandes3)
	CMD_call(commandes4)
	CMD_call(commandes5)
	CMD_call(commandes6)
	CMD_call(commandes7)
	//CMD_call(commandes8)
	CMD_call(commandes9)
}
