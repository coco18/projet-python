<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
  <form method="post" action="/search2">
    <select class="" name="equipment">
      % for o in data:
        <option value="{{o}}">{{o}}</option>
      % end
    </select>
    <input type="submit" value="Rechercher">
  </form>
  </body>
</html>
