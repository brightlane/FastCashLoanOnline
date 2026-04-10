/**
 * SoftLife Finance - Automated Freshness Script
 * Updates the 'Weekly Update' block with current dates and rotating tips.
 */

const financeUpdates = {
    getWeekRange: function() {
        const now = new Date();
        const start = new Date(now.setDate(now.getDate() - now.getDay()));
        const end = new Date(now.setDate(now.getDate() + 6));
        return `${start.toLocaleDateString('en-US', {month:'long', day:'numeric'})} - ${end.toLocaleDateString('en-US', {day:'numeric', year:'numeric'})}`;
    },
    
    tips: [
        "Applying before 11:45 AM CT is the best way to secure same-day ACH funding.",
        "Ensure your bank account has been active for at least 90 days to increase approval odds.",
        "Tribal lenders like MaxLend often consider income over credit score—have your paystub ready.",
        "Check your state's specific APR caps before signing; MaxLend serves 34 states currently."
    ],

    init: function() {
        const updateBox = document.getElementById('dynamic-content');
        if (updateBox) {
            const randomTip = this.tips[Math.floor(Math.random() * this.tips.length)];
            updateBox.innerHTML = `
                <p><strong>Week of ${this.getWeekRange()}</strong></p>
                <ul style="line-height: 1.6;">
                    <li><strong>Market Status:</strong> High liquidity. Funding windows are open.</li>
                    <li><strong>Pro Tip:</strong> ${randomTip}</li>
                    <li><strong>Verified Link:</strong> <a href="https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWebWeb" style="color: #27ae60; font-weight:bold;">Check Today's Eligibility</a></li>
                </ul>
            `;
        }
    }
};

window.onload = () => financeUpdates.init();
