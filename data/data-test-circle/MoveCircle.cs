using System.Collections.Generic;
using System.Globalization;
using System.IO;
using UnityEngine;
using System;

public class MoveBall : MonoBehaviour
{

    public float amplitudeX = 3f;
    public float amplitudeY = 3f;
    public float amplitudeZ = 3f;

    public float freqY = 1f;

    private Vector3 _initialPosition;

    private string _filePath;

    private DateTime currentDate = DateTime.Now;
    // Start is called before the first frame update

    void Start()
    {
        string fileName = "positions_xyz_" + currentDate.ToString("yyyy-MM-dd_HH'h'mm'm'") + ".csv";
        _filePath = Path.Combine(Application.dataPath, "Scripts/data/", fileName);
        _initialPosition = transform.position;
        CreateCsvFile();
    }

    // Update is called once per frame
    void Update()
    {
        float angle = Time.time * freqY;
        var newX = _initialPosition.x + amplitudeX * Mathf.Cos(angle);
        var newY = _initialPosition.y + amplitudeY * Mathf.Sin(angle);
        var newZ = _initialPosition.z + amplitudeZ * Mathf.Sin(angle);
        var transformPos = transform.position;
        // Update the position of the circle
        transform.position = new Vector3(newX, newY, newZ);

        WriteXyzPosToCsv();
    }
    private void CreateCsvFile()
    {
        string[] headers = { "x", "y", "z" };
        string[] initialPositionArray = { _initialPosition.x.ToString(CultureInfo.InvariantCulture), _initialPosition.y.ToString(CultureInfo.InvariantCulture), _initialPosition.z.ToString(CultureInfo.InvariantCulture) };
        File.WriteAllLines(_filePath, new List<string[]> { headers, initialPositionArray }.ConvertAll(row => string.Join(",", row)));
        Debug.Log("CSV file created: positions_xyz.csv");
    }

    private void WriteXyzPosToCsv()
    {
        var transformPos = transform.position;
        string[] positions = { transformPos.x.ToString(CultureInfo.InvariantCulture), transformPos.y.ToString(CultureInfo.InvariantCulture), transformPos.z.ToString(CultureInfo.InvariantCulture) };
        File.AppendAllLines(_filePath, new List<string> { string.Join(",", positions) });
    }
}
