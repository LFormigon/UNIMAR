<?php
    include "Funcionario.php";
    include "Gerente.php";
    include "Vendedor.php";

    $vendedor = new Vendedor("Douglas Vinicius", "Americanas", 1050, "Vendedor", 52.5);
    echo "<br>Funcionário 001<br>
        
        Nome: {$vendedor->getnome()}<br>
        Empresa: {$vendedor->getempresa()}<br>
        Salário: {$vendedor->getsalario()}<br>
        Cargo: {$vendedor->getcargo()}<br>
        Comissão: {$vendedor->getComissao()}<br>";
    
    $gerente = new Gerente("João Carlos", "Pandora", 1000, "Gerente");
    echo "<br>Funcionário 002<br>
        
        Nome: {$gerente->getnome()}<br>  
        Empresa: {$gerente->getempresa()}<br>
        Salário: {$gerente->getsalario()}<br>
        Cargo: {$gerente->getcargo()}<br>";
    

?>