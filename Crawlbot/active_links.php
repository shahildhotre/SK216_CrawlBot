Search Results
<br>
<?php
if(file_exists("crawledlinks.csv")){
	$CSVfp = fopen("crawledlinks.csv", "r");
	if($CSVfp !== FALSE) {
	 while(! feof($CSVfp)) {
	  $data = fgetcsv($CSVfp, 1000, ",");
	  $linkdisp = "<a href=".$data[1]." style='color:white;'>".$data[1]."</a>";
	  echo $linkdisp;
	  echo "<br>";
	 }
	}
	fclose($CSVfp);
}