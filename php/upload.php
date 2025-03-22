<?php

$fileName = $_GET["name"];
$dir = isset($_GET["dir"]) ? $_GET["dir"]."/" : "";
$path = "./".$dir;
$start = boolval($_GET["start"]);
$body = file_get_contents("php://input");
$pathFile = $path . $fileName;
if ($start) {
    if (file_exists($pathFile)) {
        unlink($pathFile);
    }

}
$file = fopen($pathFile,"ab");
fwrite($file, $body);
fclose($file);
echo "OK"



?>