class DataLoader:
    def __init__(self,filepath):
        self.filepath= filepath

    # Defined a function to clean the pacakge info
    def package_restructure(self,x):
            # First check if the value is NaN
            if pd.isna(x):
                return "No Package Info"
            # Ensure x is a string before using string operations
            x= str(x) # Convert to string to safely use 'in' or 'startswith'
            if "Level 0" in x:
                return "CZ Level 0 Package"
            elif "Level 1" in x:
                return "CZ Level 1 Package"
            elif "Level 2" in x:
                return "CZ Level 2 Package"
            elif "Level 3" in x:
                return "CZ Level 3 Package"
            elif "Level 4" in x:
                return "CZ Level 4 Package"
            elif x.startswith('Accelerate'):
                return "CZ Accelerate Package"
            elif x.startswith('Ignite'):
                return "CZ Ignite Package"
            elif x.startswith('Rev'):
                return "CZ Rev Package"
            else:
                return "Other Package"