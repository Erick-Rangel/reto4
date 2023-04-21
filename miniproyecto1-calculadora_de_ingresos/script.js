function calculate() {
  // Obtiene el salario y las horas del formulario
  const salary = document.getElementById("salary").value;
  const hours = document.getElementById("hours").value;

  // Calcula el ingreso semanal y mensual
  const weeklyIncome = salary * hours;
  const monthlyIncome = weeklyIncome * 4;

  // Muestra el resultado en la página
  const resultElement = document.getElementById("result");
  resultElement.innerHTML = `Ingreso semanal: $${weeklyIncome.toFixed(2)} <br> Ingreso mensual: $${monthlyIncome.toFixed(2)}`;
}

function calculate() {
  // Obtiene el salario y las horas del formulario
  const salary = document.getElementById("salary").value;
  const hours = document.getElementById("hours").value;

  // Calcula el ingreso semanal y mensual
  const weeklyIncome = salary * hours;
  const monthlyIncome = weeklyIncome * 4;

  // Muestra el resultado en la página
  const resultElement = document.getElementById("result");
  resultElement.innerHTML = `Ingreso semanal: $${weeklyIncome.toFixed(2)} <br> Ingreso mensual: $${monthlyIncome.toFixed(2)}`;
}
