<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Recherche du lieux où est pratiqué l'activité :</h1>
    <form method="GET" action="/search">
      <select class="" name="activity">
        % for o in data:
          <option value="{{o}}">{{o}}</option>
        % end
      </select>
      <input type="submit" name="name" value="Rechercher">
      <br/>
    </form>
    <br/>
    <br/>
    <h1>Recherche des activitées disponnible dans ma ville :</h1>
    <form class="" action="/city" method="post">
      <select class="" name="city">
        % for o in data_city:
          <option value="{{o}}">{{o}}</option>
        % end
      </select>
      <input type="submit" name="name" value="Rechercher">
    </form>

  </body>
</html>
