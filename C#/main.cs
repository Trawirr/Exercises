using System;
using System.Collections.Generic;

public class RomanDecode
{
  public static int Solution(string roman)
  {
    Dictionary<char, int> romanNumbers = new Dictionary<char, int>
      {
          {'I', 1},
          {'V', 5},
          {'X', 10},
          {'L', 50},
          {'C', 100},
          {'D', 500},
          {'M', 1000}
      };
      int val = 0;
      for(int i=0; i<roman.Length; i++)
      {
          if (romanNumbers[roman[i]] < romanNumbers[roman[Math.Min(i+1, roman.Length-1)]]) val -= romanNumbers[roman[i]];
          else val += romanNumbers[roman[i]];
      }
      return val;
  }
}