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

    <br/>
    <form class="" action="/city" method="post">
      <select class="" name="city">
        % for o in data_city:
          <option value="{{o}}">{{o}}</option>
        % end
      </select>
      <input type="submit" name="name" value="submit">
    </form>
  </body>
</html>
