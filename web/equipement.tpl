<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <table>
      <tr>
        <td>
          Nom de l'équipement :
        </td>
        <td>
          {{equipement.name_equipement}}
        </td>
      </tr>
      <tr>
        <td>
          Adresse :
        </td>
        <td>
          {{place.num_street}} {{place.street}}
          {{place.city_code}} {{place.city}}
        </td>
      </tr>
    </table>
  </body>
</html>
