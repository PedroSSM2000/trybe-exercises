// Para o primeiro exercício de hoje, faça um programa que, dado um valor n qualquer, seja n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n . Por exemplo:
// n = 5
// *****
// *****
// *****
// *****
// *****

function asteriskSquare(n) {
  for (let i = 0; i < n; i++) {
    console.log('*'.repeat(n));
  }
}

// Para o segundo exercício, faça o mesmo que antes, mas que imprima um triângulo retângulo com 5 asteriscos de base. Por exemplo:
// n = 5
// *
// **
// ***
// ****
// *****

function asteriskTriangle(n) {
  for (let i = 0; i < n; i++) {
    console.log('*'.repeat(i + 1));
  }
}

// Agora espelhe o lado do triângulo. Por exemplo:
// n = 5
//     *
//    **
//   ***
//  ****
// *****

function asteriskTriangleMirrored(n) {
  for (let i = 0; i < n; i++) {
    console.log(`${' '.repeat(n - i - 1)}${'*'.repeat(i + 1)}`);
  }
}

// Depois, faça uma pirâmide com n asteriscos de base. Por exempo:
// n = 5
//   *
//  ***
// *****

function asteriskPyramid(n) {
  if (n % 2 !== 0) {
    for (let i = 0; i < n; i++) {
      nAsterisk = 1 + 2 * i;
      nSpace = (n - nAsterisk) / 2;
      if (nAsterisk <= n) console.log(`${' '.repeat(nSpace)}${'*'.repeat(nAsterisk)}`);
    }
  }
}
