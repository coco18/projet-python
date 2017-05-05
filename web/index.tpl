<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <p>
      bonjour
    </p>
    <select class="" name="">
      % for o in data:
        <option value="{{o}}">{{o}}</option>
      % end
    </select>
  </body>
</html>
