using System.Collections.Generic;
using System.Globalization;
using System.IO;
using UnityEngine;
using System;

public class MoveBall : MonoBehaviour
{

    public float speed = 2f;
    public float maxAmplitude = 2f;
    public float maxAngle = 45f;
    public float chaosFactor = 1f;

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
        float time = Time.time * speed;

        // Generate random values for amplitude and angle within specified ranges
        float amplitude = UnityEngine.Random.Range(0f, maxAmplitude);
        float angle = UnityEngine.Random.Range(0f, maxAngle);

        // Add randomness to the trajectory using the chaos factor
        float chaoticX = _initialPosition.x + amplitude * Mathf.Sin(time + chaosFactor * Mathf.PerlinNoise(time, 0));
        float chaoticY = _initialPosition.y + amplitude * Mathf.Sin(2 * time + chaosFactor * Mathf.PerlinNoise(time, 1));
        float chaoticZ = _initialPosition.z + amplitude * Mathf.Cos(angle * Mathf.Deg2Rad) * Mathf.Sin(time + chaosFactor * Mathf.PerlinNoise(time, 2));

        // Update the object's position
        transform.position = new Vector3(chaoticX, chaoticY, chaoticZ);

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
