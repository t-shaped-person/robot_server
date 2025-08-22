document.addEventListener("DOMContentLoaded", () => {
    const bringup_btn = document.getElementById("bringup")
    const cancel_bringup_btn = document.getElementById("cancel_br")
    const teleop_btn = document.getElementById("teleop")
    const cancel_teleop_btn = document.getElementById("cancel_te")
    const cartographer_btn = document.getElementById("cartographer")
    const cancel_cartographer_btn = document.getElementById("cancel_ca")
    const cartographer_rviz_btn = document.getElementById("cartographer_rviz")
    const cancel_cartographer_rviz_btn = document.getElementById("cancel_cr")
    const navigation_btn = document.getElementById("navigation")
    const cancel_navigation_btn = document.getElementById("cancel_na")
    const navigation_rviz_btn = document.getElementById("navigation_rviz")
    const cancel_navigation_rviz_btn = document.getElementById("cancel_nr")
    const post = (url, data = {}) =>
        fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });
    const status = document.getElementById("status");

    bringup_btn.addEventListener("click", () => {
        bringup_btn.disabled = true;
        cancel_bringup_btn.disabled = false;
        post("/launch_bringup").then(() => {
            status.innerText = "bringup successfully";
        });
    });

    cancel_bringup_btn.addEventListener("click", () => {
        bringup_btn.disabled = false;
        cancel_bringup_btn.disabled = true;
        post("/cancel_bringup").then(() => {
            status.innerText = "bringup terminated";
        });
    });

    teleop_btn.addEventListener("click", () => {
        teleop_btn.disabled = true;
        cancel_teleop_btn.disabled = false;
        post("/launch_teleop").then(() => {
            status.innerText = "teleop successfully";
        });
    });

    cancel_teleop_btn.addEventListener("click", () => {
        teleop_btn.disabled = false;
        cancel_teleop_btn.disabled = true;
        post("/cancel_teleop").then(() => {
            status.innerText = "teleop terminated";
        });
    });

    cartographer_btn.addEventListener("click", () => {
        cartographer_btn.disabled = true;
        cancel_cartographer_btn.disabled = false;
        post("/launch_cartographer").then(() => {
            status.innerText = "cartographer successfully";
        });
    });

    cancel_cartographer_btn.addEventListener("click", () => {
        cartographer_btn.disabled = false;
        cancel_cartographer_btn.disabled = true;
        post("/cancel_cartographer").then(() => {
            status.innerText = "cartographer terminated";
        });
    });

    cartographer_rviz_btn.addEventListener("click", () => {
        cartographer_rviz_btn.disabled = true;
        cancel_cartographer_rviz_btn.disabled = false;
        post("/launch_cartographer_rviz").then(() => {
            status.innerText = "cartographer_rviz successfully";
        });
    });

    cancel_cartographer_rviz_btn.addEventListener("click", () => {
        cartographer_rviz_btn.disabled = false;
        cancel_cartographer_rviz_btn.disabled = true;
        post("/cancel_cartographer_rviz").then(() => {
            status.innerText = "cartographer_rviz terminated";
        });
    });

    document.getElementById("map").addEventListener("click", () => {
        post("/save_map").then(() => {
            status.innerText = "map save successfully";
        });
    });

    navigation_btn.addEventListener("click", () => {
        navigation_btn.disabled = true;
        cancel_navigation_btn.disabled = false;
        post("/launch_navigation").then(() => {
            status.innerText = "navigation_rviz successfully";
        });
    });

    cancel_navigation_btn.addEventListener("click", () => {
        navigation_btn.disabled = false;
        cancel_navigation_btn.disabled = true;
        post("/cancel_navigation").then(() => {
            status.innerText = "navigation_rviz terminated";
        });
    });

    navigation_rviz_btn.addEventListener("click", () => {
        navigation_rviz_btn.disabled = true;
        cancel_navigation_rviz_btn.disabled = false;
        post("/launch_navigation_rviz").then(() => {
            status.innerText = "navigation_rviz successfully";
        });
    });

    cancel_navigation_rviz_btn.addEventListener("click", () => {
        navigation_rviz_btn.disabled = false;
        cancel_navigation_rviz_btn.disabled = true;
        post("/cancel_navigation_rviz").then(() => {
            status.innerText = "navigation_rviz terminated";
        });
    });
});
