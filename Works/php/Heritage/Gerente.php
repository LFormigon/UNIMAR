<?php

    class Gerente extends Funcionario {
        
        function __construct($nome, $empresa, $salario, $cargo)
        {
            parent::__construct($nome, $empresa, $salario, $cargo);
        }
        public function getsalario() {
            return parent::getsalario() * 1.25;
        }
    }
?>