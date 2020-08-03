<?php

require_once 'app/init.php';

if(isset($_GET['q'])) {

      $q = $_GET['q'];

      $params = [
          'index' => 'surface',
          'body'  => [
              'size' => 200,
              'from' => 0,
              'query' => [
                  'match' => [
                          'body' => $q
                  ]
              ]
          ]
      ];

      $query = $es->search($params);

        if($query['hits']['total'] >=1) {
            $results = $query['hits']['hits'];
    }
}
?>

 <!DOCTYPE html>
 <html>
   <head>
     <meta charset="utf-8">
     <title>Crawlbot Searchpage</title>
   </head>
   <body>
     <h1>Crawlbot</h1>
     <form action="surfaceweb_index.php" method="get" autocomplete="off">
          <div class="search-bar">
              <?php
                  if(isset($_GET['q'])) {
                ?>
                          <input type="text" name="q" placeholder="Search..." value= "<?php echo $q ?>">
              <?php
                    }

                  else{
                           echo '<input type="text" name="q" placeholder="Search..." value="" >';
                      }
               ?>

          </div>
          <input type="submit" value="Search">
     </form>
     <p></p>
     <?php
      if(isset($results)){
          foreach($results as $r) {
          ?>
                <div class="result">
                    <div class = "title"><?php echo $r['_source']['title']; ?></div>
                    <a href="#<?php echo $r['_id']; ?>"><div class="link"><?php echo $r['_source']['link']; ?></div></a>
                </div>
          <?php
        }
      }
     ?>
     <div class="button">
         <a href="http://localhost/esphpsearch/index.html" class="btn">Return to Main Page</a>
     </div>

  </body>

<style>

    body{
                    background-image: linear-gradient(rgba(0,0,0,0.5),rgba(0,0,0,0.5)),url(bg.jpg);
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    height: 100vh;
                    background-size: cover;
                    background-position: center;
        }

      p{
                    margin-bottom: 80px;

       }

    .result{
                    padding-top: 40px;
        }

    .result .title{
                    font-size: 19px;
                    color: white;
        }

    input[type="text"]{
                    width: 250px;
                    height: 10px;
                    position: absolute;
                    top: 5.5%;
                    left: 12%;
                    border: 2px solid #ccc;
                    border-radius: 4px;
                    background-image: url(search2.png);
                    background-repeat: no-repeat;
                    background-position: 5px 3.5px;
                    padding: 10px 20px 10px 40px;
                    transition: 0.4s all;
        }

      input[type="submit"]{
                    height: 32px;
                    position: absolute;
                    top: 5.60%;
                    left: 36%;
                    transition: 0.4s all;
        }

      h1{
                    position: absolute;
                    top: 2.5%;
                    left: 0.5%;
                    color: white;
                    font-weight: bold;
        }

        .button .btn{
                    width: 135px;
                    height: 18px;
                    position: absolute;
                    top: 4.0%;
                    left: 85%;
                    border: 1px solid #fff;
                    padding: 5px 10px 5px 10px;
                    text-decoration: none;
                    background-color: #fff;
                    color: #000;
                    transition: 0.4s all;
        }

        .link{
                    color: #7BEEE6;
        }
 </style>
</html>
