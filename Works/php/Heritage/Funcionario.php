<?php

    class Funcionario {
        private $nome, $salario, $cargo, $empresa;
        function __construct($nome, $empresa, $salario, $cargo)
        {
            $this->nome = $nome;
            $this->salario = $salario;
            $this->cargo = $cargo;
            $this->empresa = $empresa;
        }

        public function getnome() {
            return $this->nome;
        }
        public function setnome($nome) {
            $this->nome = $nome;
        }
        public function getempresa() {
            return $this->empresa;
        }
        public function setempresa($empresa) {
            $this->nome = $empresa;
        }
        public function getsalario() {
            return $this->salario;
        }
        public function setsalario($salario) {
            $this->nome = $salario;
        }
        public function getcargo() {
            return $this->cargo;
        }
        public function setcargo($cargo) {
            $this->nome = $cargo;
        }
        
    }
?>