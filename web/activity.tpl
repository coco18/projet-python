<!DOCTYPE HTML>
<html>
	<head>
		<title>Sport en Pays de la Loire</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie8.css" /><![endif]-->

		<style>
	       .map {
	        height: 400px;
	        width: 100%;
	       }
	    </style>

	</head>
	<body>







    	<!-- Feature 1 -->
    				<article id="tree" class="container box style1 right">

                <h2>{{acivity.name_activity}} à {{city}}</h2>
    						<header>
									<ul>
                  % for e in list_equipment:
                    <li class="afficherDetailEquipement" ><a  href="#">{{e.name_equipment}} à {{e.place.city}}</a>
										<div class="detailEquipement">
											<table>
									      <tr>
									        <td>
									          Nom de l'équipement :
									        </td>
									        <td>
									          {{e.name_equipment}}
									        </td>
									      </tr>
									      <tr>
									        <td>
									          Adresse :
									        </td>
									        <td>
									          {{e.place.num_street}} {{e.place.street}}
									          {{e.place.city_code}} {{e.place.city}}
									        </td>
									      </tr>
									    </table>




											 AIzaSyDPKF_pbGPwKpfAsZMmmqGQh0YxbG_9mr4

										</div></li>
                  % end
								</ul>



								<div class="map" id="a"></div>
										<script>



										function initMap() {



												var uluru = {lat: {{list_equipment[0].place.latitude}}, lng: {{list_equipment[0].place.longitude}}};
												var map = new google.maps.Map(document.getElementById('a'), {
													zoom: 4,
													center: uluru
												});

												var marker = new google.maps.Marker({
													position: uluru,
													map: map
												});

												% for e in list_equipment:
												var c{{e.id}} = {lat: {{e.latitude}}, lng: {{e.longitude}} };

												var marker{{e.id}} = new google.maps.Marker({
													position: c{{e.id}},
													map: map
												});
												% end
}
										</script>
										<script async defer
										src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBe5oWItPZuTWdsUJyl500vhoLSxN4cs5s&callback=initMap">
										</script>
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
					<script type="text/javascript">
					$(document).ready(function(){

					$(".detailEquipement").toggle();
					$(".afficherDetailEquipement").click(function (event) {
						$(this).children(".detailEquipement").toggle()
						event.preventDefault();
					});
					});
					</script>

					<section id="footer">

								<div class="copyright">
									<ul class="menu">
										<li>&copy; Pauline CHABAUD et Corentin MAY</li><li>Données : <a href="http://data.paysdelaloire.fr/">http://data.paysdelaloire.fr/</a></li>
									</ul>
								</div>
							</section>
  </body>
</html>
