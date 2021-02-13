// Custom UwU library for C#
// Sadly theres really good Python ones, but the one or two C# ones are incompatible with this version of .net

namespace uwu {

    // Simple UwU Convertor: https://www.geeksforgeeks.org/uwu-text-convertor-in-python/
    
    class UwUGen  {
        public static string generate (string input) {
            int len = input.Length;

            string output = "";

            for (int i = 0; i < len-1; i++) {
                string curr_char = input.Substring (i, 1); 
                string prev_char = "";

                if (i > 0) {
                    prev_char = input.Substring(i-1, 1);
                }

                // Handles Ls and Rs
                if (curr_char.Equals("L") || curr_char.Equals("R")) {
                    output += "W";
                }
                else if (curr_char.Equals("l") || curr_char.Equals("r")) {
                    output += "w";
                }

                // Handles nyo and myo
                else if (curr_char == "O" || curr_char == "o") {
                    if (prev_char == "N" || prev_char == "n" || prev_char == "M" || prev_char == "m"){
                        output += "yo";
                    }
                    else {
                        output += curr_char;
                    }
                }

                else {
                    output += curr_char;
                }

            }

            return output;
        }

    }

}