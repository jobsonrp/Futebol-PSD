<?php
$link = mysqli_connect("localhost", "root", "");
 
if ($link) {
	echo "Sucesso: Sucesso ao conectar-se com a base de dados MySQL. <br>" . PHP_EOL;
	echo "OS DADOS DO BANCO DE DADOS ESTAO ABAIXO!";

}else{
	echo "Error: Falha ao conectar-se com o banco de dados MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}
 
$data= [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0],[0, 5, 0],[0, 6, 0],[0, 7, 0],
	  [1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0],
	  [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0],
	  [3, 0, 0], [3, 1, 0],[3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0],
	  [4, 0, 0], [4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0],  [4, 5, 0], [4, 6, 0], [4, 7, 0],
	  [5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0],
	  [6, 0, 0], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0],
	  [7, 0, 0], [7, 1, 0], [7, 2, 0], [7, 3, 0], [7, 4, 0], [7, 5, 0], [7, 6, 0], [7, 7, 0],
	  [8, 0, 0], [8, 1, 0], [8, 2, 0], [8, 3, 0], [8, 4, 0], [8, 5, 0], [8, 6, 0], [8, 7, 0], 
	  [9, 0, 0], [9, 1, 0], [9, 2, 0], [9, 3, 0], [9, 4, 0], [9, 5, 0], [9, 6, 0], [9, 7, 0],
	  [10, 0, 0], [10, 1, 0], [10, 2, 0], [10, 3, 0], [10, 4, 0], [10, 5, 0], [10, 6, 0], [10, 7, 0],
	  [11, 0, 0], [11, 1, 0], [11, 2, 0], [11, 3, 0], [11, 4, 0], [11, 5, 0], [11, 6, 0], [11, 7, 0],
	  [12, 0, 0], [12, 1, 0], [12, 2, 0], [12, 3, 0], [12, 4, 0], [12, 5, 0], [12, 6, 0], [12, 7, 0],
	  ];
  
function array atualizarmapa(){
	 

//iniciando a conexão com o banco de dados 
$cx = mysqli_connect("localhost", "root", "") or die(mysqli_error());
//$con = mysqli_connect(DB_SERVER, DB_USER, DB_PASSWORD, DB_DATABASE)
   //selecionando o banco de dados 
$db = mysqli_select_db($cx, "dbfutebol");
   //criando a query de consulta à tabela criada 
$result = "SELECT * FROM grid";
//$data =[];
$sql = mysqli_query($cx, $result) or die( mysqli_error($cx)); //caso haja um erro na consulta );   
//pecorrendo os registros da consulta. 

while ($aux = mysqli_fetch_assoc($sql)) { 
//echo "<br>-----------------------------------------<br>"; 
//echo "id:".$aux["id"]."<br>"; 
//echo "idsensor:".$aux["idsensor"]."<br>"; 
array_push($data, [$data[$aux["linha"]], $data[$aux["coluna"]], $data[$aux["celula"]] ]);
}
 return $data;
}
//for($lop = 0; $lop < count($data);$lop++){echo ($lop);}

?>