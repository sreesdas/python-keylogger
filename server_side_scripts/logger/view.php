<html>
<head>
<meta charset="UTF-8">
</head>

<body>

<h3>Select File</h3>
<hr />

<?php
$str = '';
$dir = './logs/';
$files = scandir($dir);
for($i=0; $i < count($files); ++$i){
	if( strpos($files[$i],'.txt') !== false){
		echo '<a href="logs/'. $files[$i] .'">' . $files[$i] . '</a><br>' ;
	} 
}

?>

</body>
</html>