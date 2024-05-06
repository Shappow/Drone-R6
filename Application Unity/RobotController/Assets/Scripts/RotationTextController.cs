using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
public class RotationController : MonoBehaviour
{
    public TextMeshProUGUI textMeshProUGUI;
    // Start is called before the first frame update
    public FixedJoystick rotationJoystick;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        textMeshProUGUI.text = "x : "  + rotationJoystick.Horizontal.ToString() + "y : "  +  rotationJoystick.Vertical.ToString();
    }
}
