import json
import requests
import streamlit as st
from modules.nav import SideBarLinks
import logging
from modules.theme import *


logger = logging.getLogger(__name__)
custom_style()
banner("Policy Management Dashboard",
       "Manage your saved and published policies")
SideBarLinks()

user_id = st.session_state['user_id']

# saved policies
st.markdown("""
    <div style='background: #18435a; padding: 1.5rem; border-radius: 8px; margin: 2rem 0;'>
        <h3 style='color: #e2e8f0; margin: 0 0 1rem 0;'>Saved Policies</h3>
        <p style='color: #94a3b8; margin: 0;'>View and manage your saved policy drafts</p>
    </div>
""", unsafe_allow_html=True)

saved_policies = requests.get(
    f"http://web-api:4000/politician/allpolicy/{user_id}").json()
count = 0
for item in saved_policies:
    count += 1
    id = int(item["saved_id"])

    # Check if policy is already published
    try:
        check_response = requests.get(
            f"http://web-api:4000/politician/all_published/{id}")
        is_published = check_response.status_code == 200 and check_response.json().get(
            "is_published", False)

        if is_published:
            continue

        policy_url = f"http://web-api:4000/politician/policy/{id}"
        policyJson = requests.get(policy_url).json()[0]
        title = policyJson["title"]

        st.markdown(
            f"<h4 style='margin-bottom:0;'>{title}</h4>", unsafe_allow_html=True)
        with st.expander(label=f'Expand {title}', expanded=False):
            col1, col2 = st.columns([4, 1], vertical_alignment="bottom")
            with col1:
                st.write(f'**Country:** {policyJson["Country"]}')
                st.write("")
                st.write("**Monetary Policy:**")
                st.write(f'**Discount Rate:** {policyJson["discountRate"]}%')
                st.write(
                    f'**Federal Reserve Balance Sheet:** ${policyJson["FederalReserveBalanceSheet"]} Billion')
                st.write(
                    f'**Treasury Holdings:** ${policyJson["TreasurySecurities"]} Billion')
                st.write(
                    f'**Federal Funds Rate:** {policyJson["FederalFundsRate"]}%')
                st.write(
                    f'**Money Supply:** ${policyJson["MoneySupply"]} Billion')
                st.write(
                    f'**Reserve Requirement Ratio:** {policyJson["ReserveRequirementRatio"]}%')
                st.write("**Fiscal Policy:**")
                st.write(
                    f'**Military Spending:** {policyJson["MilitarySpending"]}%')
                st.write(
                    f'**Education Spending:** {policyJson["EducationSpending"]}%')
                st.write(
                    f'**Health Spending:** {policyJson["HealthSpending"]}%')
                st.write(
                    f'**Infrastructure Spending:** {policyJson["InfrastructureSpending"]}%')
                st.write(
                    f'**Debt-to-GDP Ratio:** {policyJson["DebtToGDPRatio"]}%')
                st.write(
                    f'**Corporate Tax Rate:** {policyJson["CorporateTaxRate"]}%')
            with col2:
                if st.button("View Analysis", key=f"analyze_{id}", use_container_width=True):

                    st.session_state['policy_params'] = {
                        'Selected Country': policyJson['Country'],
                        'Discount Rate': policyJson['discountRate'],
                        'Federal Balance': policyJson['FederalReserveBalanceSheet'],
                        'Treasury Holdings': policyJson['TreasurySecurities'],
                        'Federal Funds Rate': policyJson['FederalFundsRate'],
                        'Money Supply': policyJson['MoneySupply'],
                        'Reserve Requirement Ratio': policyJson['ReserveRequirementRatio'],
                        'Military Spending': policyJson['MilitarySpending'],
                        'Education Spending': policyJson['EducationSpending'],
                        'Health Spending': policyJson['HealthSpending'],
                        'Infrastructure Spending': policyJson['InfrastructureSpending'],
                        'Debt to GDP Ratio': policyJson['DebtToGDPRatio'],
                        'Corporate Tax Rate': policyJson['CorporateTaxRate']
                    }

                    st.session_state['Predictions'] = {
                        'Market': str(policyJson['SP500']),
                        'GDP/C': str(policyJson['GDP'])
                    }
                    st.switch_page("pages/44_Policy_Maker_viewPred.py")
                if st.button("Publish", key=f"publish_{id}", use_container_width=True):
                    try:
                        request_data = {"saved_id": id, "user_id": user_id}
                        logger.info(
                            f"Sending publish request with data: {request_data}")

                        response = requests.post(
                            "http://web-api:4000/politician/publisher",
                            json=request_data,
                            headers={'Content-Type': 'application/json'}
                        )

                        logger.info(
                            f"Response status code: {response.status_code}")
                        logger.info(f"Response content: {response.text}")

                        if response.status_code == 201:
                            st.success("Policy published successfully!")
                            st.rerun()
                        elif response.status_code == 400:
                            error_msg = response.json().get("error", "Failed to publish policy")
                            st.error(f"Error: {error_msg}")
                        else:
                            st.error(
                                f"Failed to publish policy. Status code: {response.status_code}")
                            st.error(f"Response: {response.text}")
                    except requests.exceptions.RequestException as e:
                        logger.error(f"Request error: {str(e)}")
                        st.error(f"Network error: {str(e)}")
                    except json.JSONDecodeError as e:
                        logger.error(f"JSON decode error: {str(e)}")
                        st.error(f"Invalid response from server: {str(e)}")
                    except Exception as e:
                        logger.error(f"Unexpected error: {str(e)}")
                        st.error(f"Error publishing policy: {str(e)}")
    except Exception as e:
        logger.error(f"Error checking publication status: {str(e)}")
        st.error("Error checking if policy is published")

# published policies
st.markdown("""
    <div style='background: #18435a; padding: 1.5rem; border-radius: 8px; margin: 2rem 0;'>
        <h3 style='color: #e2e8f0; margin: 0 0 1rem 0;'>Published Policies</h3>
        <p style='color: #94a3b8; margin: 0;'>View and manage your published policies</p>
    </div>
""", unsafe_allow_html=True)

try:
    response = requests.get(
        f"http://web-api:4000/politician/userPublisher/{user_id}")
    if response.status_code == 200:
        published_policies = response.json()

        if published_policies:
            for policy in published_policies:
                try:

                    policy_details_response = requests.get(
                        f"http://web-api:4000/politician/policy/{policy['saved_id']}")
                    if policy_details_response.status_code == 200:
                        policy_details = policy_details_response.json()[0]

                        policy_title = policy_details.get(
                            'title', f'Policy {policy["publish_id"]}')
                        with st.expander(f"Expand {policy_title}", expanded=False):
                            col1, col2 = st.columns(
                                [4, 1], vertical_alignment="bottom")
                            with col1:
                                st.write(
                                    f'**Country:** {policy_details["Country"]}')
                                st.write(
                                    f'**Discount Rate:** {policy_details["discountRate"]}%')
                                st.write(
                                    f'**Federal Reserve Balance Sheet:** ${policy_details["FederalReserveBalanceSheet"]} Billion')
                                st.write(
                                    f'**Treasury Holdings:** ${policy_details["TreasurySecurities"]} Billion')
                                st.write(
                                    f'**Military Spending:** {policy_details["MilitarySpending"]}%')
                                st.write(
                                    f'**Education Spending:** {policy_details["EducationSpending"]}%')
                                st.write(
                                    f'**Health Spending:** {policy_details["HealthSpending"]}%')
                                st.write(
                                    f'**SP500 Prediction:** {policy_details["SP500"]:,.2f}')
                                st.write(
                                    f'**GDP Prediction:** {policy_details["GDP"]:,.2f}')

                            with col2:
                                if st.button("View Analysis", key=f"analyze_pub_{policy['publish_id']}", use_container_width=True):
                                    st.switch_page(
                                        "pages/44_Policy_Maker_viewPred.py")

                                if st.button("Unpublish", key=f"unpublish_{policy['publish_id']}", use_container_width=True):
                                    try:
                                        unpublish_response = requests.delete(
                                            f"http://web-api:4000/politician/publisher/{policy['publish_id']}")
                                        if unpublish_response.status_code == 200:
                                            st.success(
                                                "Policy unpublished successfully!")
                                            st.rerun()
                                        else:
                                            st.error(
                                                "Failed to unpublish policy")
                                    except Exception as e:
                                        st.error(
                                            f"Error unpublishing policy: {str(e)}")

                            st.markdown("<br>", unsafe_allow_html=True)
                    else:
                        st.error(
                            f"Failed to fetch policy details for publish_id {policy['publish_id']}")
                except Exception as e:
                    st.error(
                        f"Error processing policy {policy['publish_id']}: {str(e)}")
        else:
            st.info("No published policies found.")
    else:
        st.error("Failed to fetch published policies")
except Exception as e:
    st.error(f"Error: {str(e)}")

st.write("---")
