document.addEventListener("DOMContentLoaded", function () {
  const configForm = document.getElementById("config-form");
  const activityLogList = document.getElementById("activity-log-list");
  const screenshotGrid = document.getElementById("screenshot-grid");

  configForm.addEventListener("submit", function (e) {
    e.preventDefault();
    updateConfig();
  });

  function updateConfig() {
    const interval = parseInt(
      document.getElementById("screenshot-interval").value
    );
    const blur = document.getElementById("screenshot-blur").checked;
    const enabled = document.getElementById("screenshot-enabled").checked;

    fetch("/api/update-config/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ interval, blur, enabled }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          alert("Configuration updated successfully");
        } else {
          alert("Error updating configuration");
        }
      });
  }

  function fetchActivityLogs() {
    fetch("/api/activity-logs/")
      .then((response) => response.json())
      .then((data) => {
        console.log("Activity logs received:", data);
        activityLogList.innerHTML = "";
        data.forEach((log) => {
          const li = document.createElement("li");
          li.textContent = `${new Date(log.timestamp).toLocaleString()} - ${
            log.activity_type
          }: ${log.details}`;
          activityLogList.appendChild(li);
        });
      })
      .catch((error) => console.error("Error fetching activity logs:", error));
  }

  function fetchScreenshots() {
    fetch("/api/screenshots/")
      .then((response) => response.json())
      .then((data) => {
        console.log("Screenshots received:", data);
        screenshotGrid.innerHTML = "";
        data.forEach((screenshot) => {
          const div = document.createElement("div");
          div.className = "screenshot-item";
          div.innerHTML = `
                <img src="${screenshot.image_path}" alt="Screenshot">
                <p>${new Date(screenshot.timestamp).toLocaleString()}</p>
                <p>Blurred: ${screenshot.is_blurred ? "Yes" : "No"}</p>
            `;
          screenshotGrid.appendChild(div);
        });
      })
      .catch((error) => console.error("Error fetching screenshots:", error));
  }

  fetchActivityLogs();
  fetchScreenshots();
  setInterval(fetchActivityLogs, 30000); // Refresh every 30 seconds
  setInterval(fetchScreenshots, 60000); // Refresh every 60 seconds
});
