<!DOCTYPE HTML>
<html>
	<head>
		<title>Sport en Pays de la Loire</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie8.css" /><![endif]-->
	</head>
	<body>





    	<!-- Feature 1 -->
    				<article id="tree" class="container box style1 right">

                <h2>Liste des activités à {{city}}</h2>
    <ul>
      % for a in list_activity:
        <li><a href="/activity?activity={{a.id}}&city={{city}}">{{a.name_activity}}</a></li>
      % end
    </ul>
  </header>
</article>


<!-- Scripts -->
<script src="js/jquery.min.js"></script>
<script src="js/jquery.scrolly.min.js"></script>
<script src="js/jquery.poptrox.min.js"></script>
<script src="js/skel.min.js"></script>
<script src="js/util.js"></script>
<!--[if lte IE 8]><script src="js/ie/respond.min.js"></script><![endif]-->
<script src="js/main.js"></script>


<section id="footer">

  <div class="copyright">
    <ul class="menu">
      <li>&copy; Pauline CHABAUD et Corentin MAY</li><li>Données : <a href="http://data.paysdelaloire.fr/">http://data.paysdelaloire.fr/</a></li>
    </ul>
  </div>
</section>
</body>
</html>
