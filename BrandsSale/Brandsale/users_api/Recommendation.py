import pandas as pd
def pick_rules(row, user_interest_list):
    
    consider_antecedents = True
    consider_consequents = True

        # Loop through all antecedents and find is this antecedents are
        # related to user intersts or not?.
    for item in row.antecedents:
        if item not in user_interest_list:
            consider_antecedents = False

        if  consider_antecedents:
            # Antecedents are matched

            # Now check if consequents of this rule is not in users Interests
            # then this rule is for this user.
            for item in row.consequents:
                if item in user_interest_list:
                    consider_consequents = False
                    
            if(consider_consequents):
                # This rule is matched with the user.
                return True
            else:
                return False

        else:
            return False
        
def genrate_profile():
    
    rul_df=pd.read_csv('brands_recommendation.csv',converters={'antecedents': eval, 'consequents': eval})            # get user name and interests of new user.
    userinterests = 'BATA,NIKE,STYLO'
    username = 'muzammmil'
            # convert user interest into list.
    u_i_list = userinterests.split(',')

    applied_rul_df =  pd.DataFrame(columns=rul_df.columns)
            
    for index, row in  rul_df.iterrows():
        if(pick_rules(row,u_i_list)):
            applied_rul_df = applied_rul_df.append(row)
                    
            # get a rule which have higest lift 
        if(applied_rul_df.shape[0] >= 1):
            

            columns_names = ['antecedents', 'consequents', 'antecedent support', 'consequent support', 'support', 'confidence', 'lift', 'leverage', 'conviction']    
            selected_rule= applied_rul_df.iloc[applied_rul_df.lift.argmax()]
            userSeleted_Interest = selected_rule.consequents
            new_user = {
                    "Name": username,
                    "interests": userSeleted_Interest
                }
            
        else:
                # In case no rule is matched with the user Interests.
            new_user = {
            "Name": username,
               "interests": "PAKISTAN"
        }
    print(new_user)
            
genrate_profile()
