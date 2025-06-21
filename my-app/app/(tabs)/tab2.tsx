import { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function Tab2Calculator() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [result, setResult] = useState<number | null>(null);

  const handleCalculate = () => {
    const n1 = parseFloat(num1);
    const n2 = parseFloat(num2);
    if (!isNaN(n1) && !isNaN(n2)) {
      setResult(n1 + n2); // 足し算
    } else {
      setResult(null);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>かんたん計算アプリ</Text>

      <TextInput
        style={styles.input}
        keyboardType="numeric"
        placeholder="数字1"
        value={num1}
        onChangeText={setNum1}
      />
      <TextInput
        style={styles.input}
        keyboardType="numeric"
        placeholder="数字2"
        value={num2}
        onChangeText={setNum2}
      />

      <Button title="計算する" onPress={handleCalculate} />

      {result !== null && <Text style={styles.result}>結果: {result}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 24,
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    marginBottom: 24,
    textAlign: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#aaa',
    borderRadius: 6,
    padding: 12,
    fontSize: 18,
    marginBottom: 12,
  },
  result: {
    marginTop: 20,
    fontSize: 22,
    textAlign: 'center',
    fontWeight: 'bold',
  },
});
