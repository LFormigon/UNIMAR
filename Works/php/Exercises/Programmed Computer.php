<?php

class Computador
{
    #Configurações

    public $sistema_operacional;
    public $processador;
    public $clock;
    public $placa_mae;
    public $placa_de_video;
    public $HD;
    public $memoria_ram;

    #ON/OFF
    
    public $power;
    public $Off;
       

    public function __construct($sistema_operacional,$processador,$clock,$placa_mae,$placa_de_video,$HD,$memoria_ram)
    {
        
        $this->sistema_operacional = $sistema_operacional;
        $this->processador = $processador;
        $this->clock = $clock;
        $this->placa_mae = $placa_mae;
        $this->placa_de_video = $placa_de_video;
        $this->HD = $HD;
        $this->memoria_ram = $memoria_ram;
        $this->power = TRUE;
        $this->Off = FALSE;
    }
    public function power()
    {
      $power = TRUE;
      if ($power == TRUE) {
        return "<br/> Inicializado o Computador.. <br/>";
        
      } 
    } 
    public function Off()
    {
      $power = FALSE;
      if ($power == FALSE) {
          return "<br/> Desligando o Computador.. <br/>";
      }
      return $Off;
    }
    
    public function config () {
      echo "<br />Sistema Operacional: $this->sistema_operacional<br/>
            Procesador: $this->processador<br/>
            clock: $this->clock<br/>
            placa mãe: $this->placa_mae<br/>
            placa de video: $this->placa_de_video<br/>
            HD: $this->HD<br/>
            Memoria RAM: $this->memoria_ram<br/>";
            
  }

}
$Computador = new Computador("Windows 11","INTEL PENTIUM GOLD","3GHz","H410M","RX 550 4g","1 TB","4g RAM");
echo $Computador->power();
$Computador->config();