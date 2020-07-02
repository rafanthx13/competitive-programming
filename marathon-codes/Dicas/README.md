# Dicas para a programação

+ (04/06/2019) Se você encontrar um problema em que a solução seja fazer muitos calculos, tente olha rpor uma outra otica de forma teorica. **se esta dificil pense de forma totalmente diferente, isso vale se envolver algo numerico ou se ha entidades/relações matemáticas no problema**
 - Exemplo: Em um problema em que você tem que fazer a difenrença entre um dia1 = (dia,hora,minuto,segundo) e um dia2 = (dia,hora,minuto,segundo) para dia,hora,minuto,segundo. 
  * A soluçâo primaria seria fazer varias subtraçoes entre as respectivas (dia,hora,minuto,segundo) e isso envolve muita abstraçao, teste e sempre conseiderar que é circular [0->60; 0->24].
  * A ideia que tive foi emvez de fazer tudo isso, converter para seundos e fazer todo o processamente em segundos (sengundos é um inteiro entâo fica mais tranquilo.

[A, B, C] = list(map(int, input().split()))
  

