# thermo-atum
Thermo_ATUM is an open-source package based on Python for thermodynamic kinetics calculations.  
  
Thermo_ATUM_v1.0 is used to apply Coats-Redfern model on any two temperature points. Therefore, It can determine the kinetics parameters of the detected phase change via TGA by determining the initial and final temperatures.  
  
The models in Thermo_ATUM are applied to TGA measurements for estimating:  
&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;Enthalpy change  
&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;Entropy change  
&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;Activation energy  
&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;Gibbs free energy  

## Mailing list
For questions, bug reports, and comments, please contact:  
  
Sherif1.se@gmail.com  
Sherif.hmHe@sci.suezuni.edu.eg  
eldeenshraf@gmail.com

## License
No license for now
## Contact
•	Authors: Sherif Ashraf (Sherif1.se@gmail.com or Sherif.hmHe@sci.suezuni.edu.eg) and Sharaf eldeen (eldeenshraf@gmail.com) .

## How it works
&nbsp;&nbsp;&nbsp;&nbsp;1-	After obtaining TGA data, you have to make an Excel sheet with only two columns.  
&nbsp;&nbsp;&nbsp;&nbsp;2-	The first column is Temperature (oC), and the second column is Weight (mg).  
&nbsp;&nbsp;&nbsp;&nbsp;3-	Move the Excel sheet to “test” file in the folder of the package.  
&nbsp;&nbsp;&nbsp;&nbsp;4-	Open terminal for Ubuntu or Windows (command line).  
&nbsp;&nbsp;&nbsp;&nbsp;5-	Use cd command to be at the location of the package, for example: `cd f/new_folder/thermo_atum`  
&nbsp;&nbsp;&nbsp;&nbsp;6-	Setup required dependencies using the following command python `setup.py install`
&nbsp;&nbsp;&nbsp;&nbsp;7-	Write the following command: `python thermo_atum.py -i ./test/TGA_input_filename.xlsx -o ./test/TGA_output_filename.xlsx --start T1 --end T2`  
&nbsp;&nbsp;&nbsp;&nbsp;8-	In TGA_input_filename.xlsx write the Excel name which is made in step 1.  
&nbsp;&nbsp;&nbsp;&nbsp;9-	In TGA_output_filename.xlsx write the desired name for the output Excel.  
&nbsp;&nbsp;&nbsp;&nbsp;10-	T1 is the initial temperature for the reaction (when weight loss starts) or can be the start of a peak in DSC or DTA, and T2 is the final temperature of the reaction or transformation.  
&nbsp;&nbsp;&nbsp;&nbsp;11-	Now Coats-Redfern model is applied and a new Excel with your desired name is created in “test” file containing x=1000/T (oK) and y=ln(-ln(1-alpha)/Tk^2) in addition, to entropy, enthalpy, Gibbs free energy, and activation energy.  
&nbsp;&nbsp;&nbsp;&nbsp;12-	You can repeat these steps for any reaction detected by TGA, DTA, or DSC.
