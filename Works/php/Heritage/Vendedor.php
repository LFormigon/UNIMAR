<?php
 class Vendedor extends Funcionario {

    private $comissaov;

    function __construct($nome, $empresa, $salario, $cargos, $comissaov)
        {
            parent::__construct($nome, $empresa, $salario, $cargos, $comissaov);
            $this->comissaov = $comissaov;
        }
   
    public function getsalario() {
        return parent::getsalario() + $this->comissaov;
    }
    public function setcomissao($comissaov) {
    $this->comissaov = $comissaov;
    }
    public function getcomissao() {
    return $this->comissaov;
    }
}
?>