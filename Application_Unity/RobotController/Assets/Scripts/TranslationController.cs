using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
public class TranslationController : MonoBehaviour
{
    // Start is called before the first frame update
    public TextMeshProUGUI textMeshProUGUI;
    public FixedJoystick translationJoystick;
    void Start()
    {
        
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        textMeshProUGUI.text = "x : " + translationJoystick.Horizontal.ToString() + "y : " + translationJoystick.Vertical.ToString();
    }
}
