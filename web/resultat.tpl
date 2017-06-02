<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
  <form method="get" action="/search2">
    <select class="" name="place">
      % for o in data:
        <option value="{{o}}">{{o}}</option>
      % end
    </select>
  </form>
  </body>
</html>
