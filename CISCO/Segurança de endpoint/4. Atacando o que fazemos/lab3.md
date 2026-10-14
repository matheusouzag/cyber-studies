# Como evitar a injeção de SQL
Embora a injeção de SQL seja uma das ameaças de APIs mais comuns, ela pode ser evitada de forma eficaz com as estratégias de prevenção corretas. As abordagens úteis para evitar a injeção de SQL incluem a restrição de procedimentos do banco de dados, a higienização das entradas do banco de dados e a aplicação do acesso com privilégios mínimos.

## Restringir procedimentos e códigos de banco de dados
A injeção de SQL depende em grande parte da capacidade de um invasor de manipular entradas de dados e funções de banco de dados. Ao restringir essas entradas e limitar o tipo de procedimentos de banco de dados que podem ser executados, as organizações podem minimizar o risco de consultas não autorizadas ou maliciosas. As formas de fazer isso incluem:

Aplicação de instruções preparadas e consultas parametrizadas: as instruções preparadas definem o código SQL aceitável e, em seguida, definem parâmetros específicos para as consultas de entrada. Quaisquer instruções SQL maliciosas são classificadas como entradas de dados inválidas, em vez de comandos executáveis.
Utilização de procedimentos armazenados: assim como as instruções preparadas, os procedimentos armazenados são instruções SQL preparadas e reutilizáveis que podem ser recuperadas de um banco de dados e impedem que partes maliciosas executem códigos diretamente no próprio banco de dados.

## Validar e higienizar as entradas do banco de dados

As entradas do usuário em qualquer banco de dados SQL devem ser monitoradas, validadas e higienizadas regularmente para eliminar código malicioso.A validação de entradas garante que os dados sejam devidamente inspecionados e formatados de acordo com critérios predeterminados, enquanto a higienização de entradas modifica (ou "higieniza") a entrada removendo caracteres inválidos ou inseguros e reformatando-a conforme necessário. As formas de garantir a validação de entradas incluem:

Estabelecimento de uma lista de permissões: uma lista de permissões pode ajudar a definir entradas de usuário válidas, em relação às quais o banco de dados pode verificar (e rejeitar) consultas de entrada que pareçam anormais. Por exemplo, caracteres especiais e URL estendido são dois tipos de entradas de usuário que podem ser exploradas por invasores para coletar informações sobre um banco de dados (antes de executar consultas maliciosas). Limitar o uso dessas entradas pode ajudar a minimizar a probabilidade de um ataque.
Evitar a entrada fornecida pelo usuário: as organizações também podem optar por evitar (ou seja,tratar como entrada, em vez de comandos ou condicionais) todas as entradas fornecidas pelo usuário, de modo que caracteres ou palavras específicos não possam ser usados para formar solicitações maliciosas.

## Aplicar o acesso com menor privilégio

O acesso com menor privilégio é o princípio de dar aos usuários apenas o acesso aos recursos protegidos que sua função exige. Por exemplo, isso pode significar limitar o número de usuários que recebem privilégios de administrador em um banco de dados ou até mesmo conceder aos usuários acesso temporário de administrador que pode ser revogado posteriormente.

Restringir o acesso de usuários a um nível baseado em função também ajuda a minimizar o impacto de uma violação, pois o invasor que violar um banco de dados usando credenciais roubadas terá a mesma capacidade limitada de visualizar, modificar, roubar ou destruir dados protegidos. Pelo mesmo motivo, as organizações devem limitar o acesso compartilhado a bancos de dados em vários sites e aplicativos.

CISCO: As respostas variam, mas devem incluir: filtrar a entrada do usuário, implantar um firewall de aplicativo Web, desativar recursos/recursos desnecessários do banco de dados, monitorar instruções SQL, usar parâmetros com procedimentos armazenados e usar parâmetros com SQL dinâmico.